from itertools import chain
from django.core.exceptions import PermissionDenied
from django.db.models import CharField, Value
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from reviews.models import CreateReviewWithTicket
from .forms import TicketForm
from .models import CreateTicket

@login_required
def flux(request):
    tickets_all = models.CreateTicket.objects.all().annotate(content_type=Value('TICKET', CharField()))
    reviews_all = CreateReviewWithTicket.objects.all().annotate(content_type=Value('REVIEW', CharField()))
    reviews = CreateReviewWithTicket.objects.filter(user=request.user)
    tickets = CreateTicket.objects.filter(user=request.user)

    tickets_user = [ticket for ticket in tickets]
    reviewed_tickets = [review.ticket for review in reviews]

    combined_items = sorted(chain(tickets_all, reviews_all),
        key=lambda item: item.time_created if hasattr(item, 'time_created') else item.date_created,
        reverse=True)

    context = {
        'reviewed_tickets': reviewed_tickets,
        'tickets_user': tickets_user,
        'combined_items': combined_items,
    }
    return render(request, 'flux/flux.html', context=context)

@login_required
def my_flux(request):
    tickets_all = models.CreateTicket.objects.all().annotate(content_type=Value('TICKET', CharField()))
    reviews_all = CreateReviewWithTicket.objects.all().annotate(content_type=Value('REVIEW', CharField()))

    combined_items = sorted(chain(tickets_all, reviews_all),
                            key=lambda item: item.time_created if hasattr(item, 'time_created') else item.date_created,
                            reverse=True)

    context = {
        'combined_items': combined_items,
    }

    return render(request, 'flux/my_flux.html', context=context)

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
def edit_ticket(request, id):
    ticket = CreateTicket.objects.get(id=id)

    if request.user == ticket.user:
        if request.method =='POST':
            form = TicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('my_flux')

        else:
            form = TicketForm(instance=ticket)

        return render(request, 'ticket/edit_ticket.html', {'form': form})

    else:
        raise PermissionDenied

@login_required
def delete_ticket(request, id):
    ticket = CreateTicket.objects.get(id=id)

    if request.user == ticket.user:
        if request.method =='POST':
            ticket.delete()
            return redirect('my_flux')

        return render(request, 'ticket/delete_ticket.html', {'ticket': ticket})

    else:
        raise PermissionDenied




