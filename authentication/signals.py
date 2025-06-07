from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import post_migrate

def create_admin_user(sender, **kwargs):
    print("Creating admin user...")

    username = getattr(settings, 'ADMIN_USERNAME', None)
    password = getattr(settings, 'ADMIN_PASSWORD', None)
    email = getattr(settings, 'ADMIN_EMAIL', 'admin@example.com')

    print(f"Username: {username}, Password: {password}, Email: {email}")

    if username and password:
        User = get_user_model()
        user, created = User.objects.get_or_create(username=username, defaults={
            'email': email,
            'is_staff': True,
            'is_superuser': True,
        })

        user.first_name = 'chad'
        user.last_name = 'gee'

        if created or not user.check_password(password):
            user.set_password(password) 
            user.save()

        if created:
            print(f"Admin user {username} created.")
        else:
            print(f"Admin user {username} already exists.")
