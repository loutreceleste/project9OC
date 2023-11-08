from django import forms
from . import models

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.CreateReviewWithTicket
        fields = ['headline', 'rating', 'body']

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.CreateTicketForReview
        fields = ['book_title', 'book_description', 'book_image']