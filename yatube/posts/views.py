from django.shortcuts import get_object_or_404, render
from .models import Group, Post
from django.db import models


class Meta:
    model = Post
    ordering = ['-pub_date']


def index(request):
    POSTS_PER_PAGE = 10
    template = "posts/index.html"
    posts = Post.objects.all()[:POSTS_PER_PAGE]
    # text = 'Это главная страница проекта Yatube'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def groups_posts(request, slug):
    POSTS_PER_PAGE = 10
    template1 = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_PER_PAGE]
    # text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template1, context)
