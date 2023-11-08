from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReviewForm, TicketForm


@login_required
def review_whithout_ticket(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()

    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.author = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect('flux')  # Rediriger l'utilisateur vers la page "flux"

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'reviews/reviews_without_ticket.html', context=context)

@login_required
def review_whith_ticket(request):
    return render(request, 'reviews/review_whith_ticket.html')

@login_required
def edit_review(request):
    return render(request, 'reviews/edit_review.html')
