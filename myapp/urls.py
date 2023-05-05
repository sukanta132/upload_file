# from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.welcome),
    path('submit', views.submit),
    path('insert', views.insert),
]
