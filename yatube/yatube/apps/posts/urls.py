from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # name = index
    # не совсем ясно правильно сделал или нет
    path('group/<slug:slug>/', views.groups_posts),  # name = group_posts
]