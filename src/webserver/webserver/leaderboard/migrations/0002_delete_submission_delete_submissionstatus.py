# Generated by Django 5.1.2 on 2024-11-14 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Submission',
        ),
        migrations.DeleteModel(
            name='SubmissionStatus',
        ),
    ]
