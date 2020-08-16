from django.contrib import admin
from django.urls import path, include
from Home import  views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contacts', views.contacts, name='contacts'),
]
