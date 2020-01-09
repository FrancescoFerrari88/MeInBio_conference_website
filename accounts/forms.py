from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Contributor

class createUser(UserCreationForm):
    institution = forms.CharField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','institution','password1','password2']

class ContributorForm(ModelForm):
    class Meta:
        model = Contributor
        fields = ['author','contribution','title','abstract','key_words','bio']
