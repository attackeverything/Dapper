# Generated by Django 5.1.2 on 2025-03-28 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0018_init_submission_statuses'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='error_message',
            field=models.TextField(blank=True, default=None),
        ),
    ]
