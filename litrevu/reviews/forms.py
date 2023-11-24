from django import forms
from . import models

class ReviewForm(forms.ModelForm):
    CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = forms.ChoiceField(
        widget=forms.RadioSelect,
        label="Note",
        choices=CHOICES
    )
    class Meta:
        model = models.CreateReviewWithTicket
        fields = ['headline', 'rating', 'body']
        labels = {
            'headline': 'Titre',
            'body': 'Description',
        }
