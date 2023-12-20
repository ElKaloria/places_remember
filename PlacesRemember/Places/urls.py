from django.urls import path
from .views import *


urlpatterns = [
    path('', ShowPosts.as_view(), name='Show_Posts'),
    path('post/<slug>:post_slug/', show_post, name='show_post')
]
