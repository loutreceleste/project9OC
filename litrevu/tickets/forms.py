from django import forms
from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.CreateTicket
        fields = ['book_title', 'book_description', 'book_image']

    book_title = forms.CharField(label="Titre", max_length=100)
    book_description = forms.CharField(label="Description", max_length=100)
