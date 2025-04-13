# Generated by Django 5.1.2 on 2024-11-10 00:11

import submissions.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_load_submission_statuses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='body',
            field=models.FileField(upload_to='uploads/', validators=[submissions.utils.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submitted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
