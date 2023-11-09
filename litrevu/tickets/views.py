from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from reviews.models import CreateReviewWithTicket


@login_required
def flux(request):
    tickets = models.CreateTicket.objects.all()
    reviews = CreateReviewWithTicket.objects.all()
    context = {
        'tickets': tickets,
        'reviews': reviews,
    }
    return render(request, 'flux/flux.html', context=context)

@login_required
def my_flux(request):
    return render(request, 'flux/my_flux.html')


@login_required
def ticket(request):
    form = forms.TicketForm()

    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('flux')

    return render(request, 'ticket/ticket.html', {'form': form})


@login_required
def edit_ticket(request):
    return render(request, 'ticket/edit_ticket.html')



