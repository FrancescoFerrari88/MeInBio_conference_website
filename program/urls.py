from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('programme/', views.programme, name='programme'),
    path('speakers/', views.speakers, name='speakers'),
    path('speakers/<int:pk>', views.SpeakerDetailedView.as_view(), name='speaker-detail'),
    path('abstracts/', views.abstracts, name='abstracts'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('legal/', views.legal, name='legal'),
    path('stats/', views.stats, name='stats')
]
