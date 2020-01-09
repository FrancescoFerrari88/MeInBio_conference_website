from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('programme/', views.programme, name='programme'),
    path('speakers/', views.speakers, name='speakers'),
    path('abstracts/', views.abstracts, name='abstracts'),
    path('about/', views.about, name='about'),
]
