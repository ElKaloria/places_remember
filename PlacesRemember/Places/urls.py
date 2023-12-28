from django.urls import path
from .views import *

app_name = "Places"
urlpatterns = [
    path('', ShowPosts.as_view(), name='Show_Posts'),
    path('post/<slug>:post_slug/', show_post, name='show_post'),
    path('addpost/', add_post, name='add_post')
]
