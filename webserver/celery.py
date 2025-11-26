import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webserver.settings')

app = Celery('webserver')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Add these configurations properly to the app
app.conf.beat_schedule = {
    'upload-due-posts-every-minute': {
        'task': 'home.tasks.upload_due_posts',
        'schedule': crontab(minute='*'),  # every minute
    },
}

app.conf.timezone = 'America/Toronto'