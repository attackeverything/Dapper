from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

class Upload(AppConfig):
    name = 'Upload'

    def ready(self):
        from django_celery_beat.models import PeriodicTask, IntervalSchedule
        import json

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.MINUTES,
        )

        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Upload Scheduled Instagram Posts',
            task='yourapp.tasks.check_and_upload_posts',
            defaults={'kwargs': json.dumps({})}
        )
