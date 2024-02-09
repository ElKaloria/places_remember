#from django.db import models
from django.urls import reverse
from django.contrib.gis.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=255)
    location = models.PointField()
    address = models.CharField(max_length=100)
    time_create = models.TimeField(auto_now_add=True)
    time_update = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post.id': self.pk})
