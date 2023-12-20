from django.contrib import admin
from .models import *


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    pass


