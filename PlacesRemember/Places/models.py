from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.TextField(max_length=100)
    comment = models.TextField(max_length=255)
    location = models.JSONField()
    address = models.TextField(max_length=100)
    publish = models.TimeField(default=timezone.now)
    time_create = models.TimeField(auto_now_add=True)
    time_update = models.TimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post.id': self.pk})

    class Meta:
        ordering = ['-publish']
