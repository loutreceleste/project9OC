from django.http import HttpResponse
from litrevu.ticket.models import CritiqueAvecTicket
'''from django.shortcuts import render'''

def flux(request):
    return HttpResponse('<h1>Hello flux!</h1>')

def ticket(request):
    critique = CritiqueAvecTicket.objects.all()
    return HttpResponse(f'''
    <h1>Hello ticket!</h1>
    <h2>Voici l'exemple d'un ticket</h2>
    <p>{critique[0].critic_title}</p>
    <p>{critique[0].book_ranking}</p>
    <p>{critique[0].critic_comment}</p>
    ''')

def critique_sans_ticket(request):
    return HttpResponse('<h1>Hello critique_sans_ticket!</h1>')

def critique_avec_ticket(request):
    return HttpResponse('<h1>Hello critique_avec_ticket!</h1>')

def posts(request):
    return HttpResponse('<h1>Hello posts!</h1>')

def modifier_critique(request):
    return HttpResponse('<h1>Hello modifier_critique!</h1>')

def modifier_ticket(request):
    return HttpResponse('<h1>Hello modifier_ticket!</h1>')