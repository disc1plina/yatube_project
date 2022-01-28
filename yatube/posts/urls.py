from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name = 'posts'),
    path('group/slug/', views.groups_posts, name = 'group_posts'),
]