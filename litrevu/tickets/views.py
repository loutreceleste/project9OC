from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def flux(request):
    return render(request, 'flux/flux.html')

@login_required
def my_flux(request):
    return render(request, 'flux/my_flux.html')

@login_required
def ticket(request):
    return render(request, 'ticket/ticket.html')

@login_required
def edit_ticket(request):
    return render(request, 'ticket/edit_ticket.html')



