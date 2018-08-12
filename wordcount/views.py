from django.http import HttpResponse 
from django.shortcuts import render 

def home(request):
    return render(request, 'home.html')

def count(request):
    param = request.GET['fulltext']
    wordcount = param.split()
    
    worddic = {}

    for word in wordcount:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1

    return render(request, 'count.html', {'param': param, 'count': len(wordcount), "worddic": worddic.items()})