from django.db import models
from django.utils import timezone

import uuid

def generate_id():
    return str(uuid.uuid4())


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} on {self.date}"
    