from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import Contributor
from django.views.generic import DetailView


def home(request):
    return render(request, 'program/home.html')

def welcome(request):
    return render(request, 'program/welcome.html')

def programme(request):
    return render(request, 'program/programme.html')

def speakers(request):
    sps = Contributor.objects.all().order_by('author__last_name')
    return render(request, 'program/speakers.html',{'sps':sps})

class SpeakerDetailedView(DetailView):
    model = Contributor
    template_name = "program/program_detail.html"
    fields = ['author','title','abstract']

def abstracts(request):
    return render(request, 'program/abstracts.html')

def about(request):
    return render(request, 'program/about.html')
