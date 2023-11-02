from django.shortcuts import render

def flux(request):
    return render(request, 'flux/flux.html')

def my_flux(request):
    return render(request, 'flux/my_flux.html')

def ticket(request):
    return render(request, 'ticket/ticket.html')

def edit_ticket(request):
    return render(request, 'ticket/edit_ticket.html')



