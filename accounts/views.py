from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .forms import createUser, ContributorForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
                                ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView
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

class createContributorView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Contributor
    fields = ['contribution','title','abstract','key_words','bio','expertise','tolearn','welcome', 'citytour', 'restaurant']
    success_message = "Your application has been saved! Thanks for being awesome!"
    template_name = 'accounts/submission.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class updateContributorView(LoginRequiredMixin,UserPassesTestMixin, SuccessMessageMixin,UpdateView):
    model = Contributor
    fields = ['contribution','title','abstract','key_words','bio','expertise','tolearn','welcome', 'citytour', 'restaurant']
    success_message = "Your application has been updated!"
    template_name = 'accounts/submission.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        application = self.get_object()
        if self.request.user == application.author:
            return True
        return False

class deleteContributorView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contributor
    success_url = '/'
    success_message = "Your application has been deleted!"


    def test_func(self):
        application = self.get_object()
        if self.request.user == application.author:
            return True
        return False


class CustomLoginView(SuccessMessageMixin, auth_views.LoginView):
    success_message = "you are now logged in"
    template_name = "accounts/login.html"

class CustomLogoutView(SuccessMessageMixin, auth_views.LogoutView):
    success_message = "you are now logged out"
