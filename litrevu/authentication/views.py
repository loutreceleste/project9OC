from django.http import HttpResponse
from litrevu.authentication.models import Users
'''from django.shortcuts import render'''

def accueil(request):
    return HttpResponse('<h1>Hello accueil!</h1>')

def inscription(request):
    user = Users.objects.all()
    return HttpResponse(f'''
        <h1>Hello inscription!</h1>
        <p>Les utilisateurs inscrits sont :<p>
        <ul>
            <li>{user[0].username}</li>
            <li>{user[1].username}</li>
            <li>{user[2].username}</li>
        </ul>
        ''')