from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import create_admin_user  # Assuming you have a signals.py file

        post_migrate.connect(create_admin_user, sender=self)