from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

# def home (request):
#     return HttpResponse("hello world")

def home (request):
    return render(request,"generator/index.html")

def password (request):

    characters=list('abcdefghjklmnoprqstuvwxyz')
    length=int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!#$%&*-_'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    thepassword=''
    for x in range (length):
        thepassword+=random.choice(characters)

    return render(request,"generator/password.html",{'password':thepassword})

def about (request):
    return render(request,"generator/about.html")