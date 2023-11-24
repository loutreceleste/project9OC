from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib import messages

from tickets.forms import TicketForm
from reviews.forms import ReviewForm

from .models import CreateReviewWithTicket
from .models import CreateTicket
from .forms import ReviewForm


@login_required
def review_whithout_ticket(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()

    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user

            if 'book_image' in request.FILES:
                ticket.book_image = request.FILES['book_image']
            else:
                messages.error(request, "Veuillez choisir une image pour le ticket.")
                return render(request, 'reviews/reviews_without_ticket.html',
                              {'ticket_form': ticket_form, 'review_form': review_form})

            ticket.save()

            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect('flux')

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'reviews/reviews_without_ticket.html', context=context)

@login_required
def review_whith_ticket(request, id):
    ticket = CreateTicket.objects.get(id=id)
    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect('flux')

    return render(request, 'reviews/review_whith_ticket.html',
                  {'review_form': review_form, 'ticket': ticket})

@login_required
def edit_review(request, id):
    review = CreateReviewWithTicket.objects.get(id=id)

    if request.user == review.user:
        ticket = review.ticket

        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('my_flux')

        else:
            form = ReviewForm(instance=review)

        return render(request, 'reviews/edit_review.html', {'form': form, 'ticket': ticket})

    else:
        raise PermissionDenied

@login_required
def delete_review(request, id):
    review_whith_ticket = CreateReviewWithTicket.objects.get(id=id)

    if request.user == review_whith_ticket.user:
        if request.method =='POST':
            review_whith_ticket.delete()
            return redirect('my_flux')

        return render(request, 'reviews/delete_review.html',
                      {'review_whith_ticket': review_whith_ticket})

    else:
        raise PermissionDenied
