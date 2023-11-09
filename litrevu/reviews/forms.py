from django import forms
from . import models

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.CreateReviewWithTicket
        fields = ['headline', 'rating', 'body']
        labels = {
            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Description',
        }