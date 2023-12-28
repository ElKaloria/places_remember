from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Post
from .forms import *

# Create your views here.

menu = [
    {'title': "О сайте", 'url_name': "home"},
    {'title': "Добавить пост", 'url_name': "add_post"},
    {'title': "Вход", 'url_name': "login"},
]


def home_page(request):
    return render(request, 'Places/home.html', {'Title': "Главная страница", 'menu': menu})


def show_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'Places/post.html', {'post': post, 'menu': menu})


def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.method)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = AddPostForm()
    return render(request, "Places/addpage.html", {'form': form, 'Title': "Добавить пост"})


class ShowPosts(ListView):
    model = Post
    template_name = "Places/profile.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context
