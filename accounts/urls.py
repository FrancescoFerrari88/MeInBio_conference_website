from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import createContributorView, updateContributorView, deleteContributorView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', views.CustomLogoutView.as_view(), name="logout"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name="password_reset"),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name="passowrd_reset_done"),
    path('submit/', createContributorView.as_view(), name='submit'),
    path('update/<int:pk>/', updateContributorView.as_view(), name='update'),
    path('delete/<int:pk>/', deleteContributorView.as_view(), name='delete')
]
