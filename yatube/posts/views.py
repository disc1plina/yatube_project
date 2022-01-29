from django.shortcuts import get_object_or_404, render
from .models import Group, Post


def index(request):
    template = "posts/index.html"
    posts = Post.objects.order_by('-pub_date')[:10]
    # text = 'Это главная страница проекта Yatube'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def groups_posts(request, slug):
    template1 = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template1, context)
