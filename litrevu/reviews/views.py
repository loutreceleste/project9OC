from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def review_whithout_ticket(request):
    return render(request, 'reviews/review_whithout_ticket.html')

@login_required
def review_whith_ticket(request):
    return render(request, 'reviews/review_whith_ticket.html')

@login_required
def edit_review(request):
    return render(request, 'reviews/edit_review.html')
