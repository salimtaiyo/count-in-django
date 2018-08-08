from django.http import HttpResponse 
from django.shortcuts import render 

def home(request):
    return render(request, 'home.html')

def name(request):
    return HttpResponse("<h1> PYHTONG </h1>")