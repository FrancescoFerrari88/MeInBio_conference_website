from django.shortcuts import render

def home(request):
    return render(request, 'program/home.html')

def welcome(request):
    return render(request, 'program/welcome.html')

def programme(request):
    return render(request, 'program/programme.html')

def speakers(request):
    return render(request, 'program/speakers.html')

def abstracts(request):
    return render(request, 'program/abstracts.html')

def about(request):
    return render(request, 'program/about.html')
