from django.http import HttpResponse
from django.shortcuts import render

def follows(request):
    return HttpResponse('<h1>Hello followers!</h1>')
