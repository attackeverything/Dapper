from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField(default='Social Media Post')
    content = models.TextField()
    platform = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/images/', null=True, blank=True)
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])