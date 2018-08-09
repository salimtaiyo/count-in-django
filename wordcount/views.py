from django.http import HttpResponse 
from django.shortcuts import render 

def home(request):
    return render(request, 'home.html')

def count(request):
    param = request.GET['fulltext']
    wordcount = param.split()
    print(wordcount)
    return render(request, 'count.html', {'param': param, 'count': len(wordcount)})