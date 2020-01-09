from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .forms import createUser, ContributorForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin

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

@login_required
def submit(request):
    if request.method == 'POST':
        submission_form = ContributorForm(request.POST, instance = request.user.contributor)
        if submission_form.is_valid():
            submission_form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your application has been saved! Thanks for being awesome!')
            return redirect('home')
    else:
        submission_form = ContributorForm(instance = request.user.contributor)
    return render(request, 'accounts/submission.html',{'submission_form':submission_form})


class CustomLoginView(SuccessMessageMixin, auth_views.LoginView):
    success_message = "you are now logged in"
    template_name = "accounts/login.html"

class CustomLogoutView(SuccessMessageMixin, auth_views.LogoutView):
    success_message = "you are now logged out"
