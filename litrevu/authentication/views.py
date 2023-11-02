from django.http import HttpResponse
from authentication.models import Users
from django.shortcuts import render

def connection(request):
    return render(request, 'authentication/connection.html')

def inscription(request):
    return render(request, 'authentication/inscription.html', {'user' : Users.objects.all()})