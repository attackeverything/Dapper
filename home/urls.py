from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pending/", views.pending, name="pending"),
    path("upload/", views.upload, name="upload"),
    path('approve/<int:post_id>/', views.approve_post, name='approve_post'),
    path('reject/<int:post_id>/', views.reject_post, name='reject_post'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail')
]