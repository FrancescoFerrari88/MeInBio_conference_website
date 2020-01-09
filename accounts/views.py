from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .forms import createUser, ContributorForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
                                ListView,
                                DetailView,
                                CreateView
                                  )
from .models import Contributor

def signup(request):
    if request.method == 'POST':
        form = createUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = createUser()
    return render(request, 'accounts/signup.html',{'form':form})

class createContributorView(CreateView):
    model = Contributor
    template_name = 'accounts/submission.html'
    context_object_name = 'submission_form'

class CustomLoginView(SuccessMessageMixin, auth_views.LoginView):
    success_message = "you are now logged in"
    template_name = "accounts/login.html"

class CustomLogoutView(SuccessMessageMixin, auth_views.LogoutView):
    success_message = "you are now logged out"
