# Generated by Django 5.1.2 on 2024-11-07 19:43

from django.db import migrations

statuses = [ 
    {"name": "pending", "description": "placeholder"},
    {"name": "failed", "description": "placeholder"},
    {"name": "completed", "description": "submission has been completed"}
]

def create_statuses(apps, schema_editor):

    SubStatus = apps.get_model("submissions", "SubmissionStatus")

    for status in statuses:
        SubStatus.objects.get_or_create(name=status["name"], description=status["description"])



class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0002_alter_submission_completed_at'),
    ]

    operations = [
        migrations.RunPython(create_statuses)
    ]
