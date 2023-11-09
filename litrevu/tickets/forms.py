from django import forms
from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.CreateTicket
        fields = ['book_title', 'book_description', 'book_image']
        labels = {
            'book_title': 'Titre',
            'book_description': 'Description',
            'book_image': 'Image',
        }
