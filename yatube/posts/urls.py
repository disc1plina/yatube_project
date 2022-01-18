from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # добавить потом name='index'
]