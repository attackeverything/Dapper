# Generated by Django 5.1.2 on 2025-02-05 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0010_remove_submission_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='model_name',
            field=models.TextField(max_length=32),
        ),
    ]
