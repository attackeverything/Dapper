from django.utils import timezone
from .models import Post
from celery import shared_task
import requests

@shared_task
def upload_due_posts():
    due_posts = Post.objects.filter(posted=False, scheduled_time__lte=timezone.now())

    for post in due_posts:
        # Call your existing Instagram upload function
        success = upload_to_instagram(post.image.path, post.content)

        if success:
            post.posted = True
            post.save()

def upload_to_instagram(image, caption):
    import requests

    IG_USER_ID = '17841475437671888'  # Replace with real IG Business ID
    PAGE_ACCESS_TOKEN = 'EAARmDrjn3BkBO6Cl9EsskgLt2nUZBkaeRQvvcW5pMlFnpN6Bxa312AcZAPcwlYtCMcJlY7PcfZCqTgja59HpbumFJShPPgjzfjx3JFmibedwHlKupApzaZCqfFFa8crjFxZAHXRUkMOm9ygIO2u8tZAPdpU8wew9OgfAq9XyIqvhLrGeYS77QZBbsG7e7Qq0wqvM00BGb80HGDNLQEfWT8FVLZBh'     # Must be Page token, not user

    # Valid 1:1 image that works
    image_url = 'https://fastly.picsum.photos/id/340/700/700.jpg?hmac=Y4i8C71JOBXjP4hcF_K01IYLqY3Ce8rrIi9JZz7Yv-o'
    head = requests.head(image_url)
    print("HEAD Response:", head.headers)

    print("Sending image:", image_url)

    # Step 1: Create media container
    create_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media"
    payload = {
        "image_url": image_url,
        "caption": "Posting via API - test image",
        "access_token": PAGE_ACCESS_TOKEN
    }
    response = requests.post(create_url, data=payload)
    data = response.json()
    container_id = data.get("id")
    publish_to_instagram(container_id, 'EAARmDrjn3BkBO6Cl9EsskgLt2nUZBkaeRQvvcW5pMlFnpN6Bxa312AcZAPcwlYtCMcJlY7PcfZCqTgja59HpbumFJShPPgjzfjx3JFmibedwHlKupApzaZCqfFFa8crjFxZAHXRUkMOm9ygIO2u8tZAPdpU8wew9OgfAq9XyIqvhLrGeYS77QZBbsG7e7Qq0wqvM00BGb80HGDNLQEfWT8FVLZBh')

def publish_to_instagram(container_id, access_token):
    publish_url = f"https://graph.facebook.com/v19.0/17841475437671888/media_publish"
    params = {
        "creation_id": container_id,
        "access_token": access_token
    }

    publish_response = requests.post(publish_url, data=params)
    print("Publish Response:", publish_response.json())

