from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

@login_required
def follows(request):
    return HttpResponse('<h1>Hello followers!</h1>')
