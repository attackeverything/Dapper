from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from .models import Post
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from django.utils import timezone
from django.shortcuts import get_object_or_404
import os
from django.conf import settings
from django.core.files import File

User = get_user_model()

def home(request: HttpRequest):
    user = request.user

    if request.user.is_authenticated:
        return render(request, 'home.html', {"user": user})
    else:
        return render(request, 'intro.html')
    
def upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        platform = request.POST.get('platform')
        #image = request.FILES.get('image')
        caption = request.POST.get('caption')
        raw_time = request.POST.get('scheduled_time')
        print("Full POST data:", request.POST)
        print(title)

        # Parse and make timezone-aware
        parsed_time = parse_datetime(raw_time)
        if parsed_time is not None:
            scheduled_time = make_aware(parsed_time)
        else:
            scheduled_time = timezone.now()

        image_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'dapper-donkey.png')
        with open(image_path, 'rb') as f:
            django_file = File(f, name='dapper-donkey.png')
            Post.objects.create(
                title=title,
                image=django_file,
                content=caption,
                scheduled_time=scheduled_time,
                status='pending',
                platform=platform
            )
            return render(request, 'submitted.html')
    return render(request, 'upload.html')
    
def pending(request: HttpRequest):
    user = request.user

    pending_posts = Post.objects.filter(status='pending').order_by('scheduled_time')
    pending_count = Post.objects.filter(status='pending').count()
    approved_count = Post.objects.filter(status='approved').count()
    rejected_count = Post.objects.filter(status='rejected').count()

    if request.user.is_authenticated:
        return render(request, 'pending.html', {
        'pending_posts': pending_posts,
        'pending_count': pending_count or 0,
        'approved_count': approved_count or 0,
        'rejected_count': rejected_count or 0,
    })
    else:
        return render(request, 'intro.html')
    
def approve_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.status = 'approved'
    post.save()
    return redirect('pending')

def reject_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.status = 'rejected'
    post.save()
    return redirect('pending')
    
def logout_view(request):
    logout(request)
    return render(request, 'intro.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def submitted(request):
    return render(request, 'submitted.html')
