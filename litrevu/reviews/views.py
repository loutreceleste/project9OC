from django.http import HttpResponse
from django.shortcuts import render

def review_whithout_ticket(request):
    return render(request, 'reviews/review_whithout_ticket.html')

def review_whith_ticket(request):
    return render(request, 'reviews/review_whith_ticket.html')

def edit_review(request):
    return render(request, 'reviews/edit_review.html')
