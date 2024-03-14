from django.contrib import admin
from .models import *


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'location', 'address', 'publish']


