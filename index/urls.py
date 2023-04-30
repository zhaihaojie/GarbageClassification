from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('image', views.receive_img),
    path('text', views.text)
]
