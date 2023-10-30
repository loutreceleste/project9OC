from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Ticket(models.Model):
    book_title = models.fields.CharField(max_length=100, default="")
    book_description = models.fields.CharField(max_length=100, default="")
    book_image = models.ImageField()

class CritiqueAvecTicket(models.Model):
    critic_title = models.fields.CharField(max_length=100, default="")
    book_ranking = models.fields.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ]
    )
    critic_comment = models.fields.CharField(max_length=100, default="")

class CritiqueSansTicket(models.Model):
    book_title = models.fields.CharField(max_length=100, default="")
    book_description = models.fields.CharField(max_length=100, default="")
    book_image = models.ImageField()
    critic_title = models.fields.CharField(max_length=100, default="")
    book_ranking = models.fields.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ]
    )
    critic_comment = models.fields.CharField(max_length=100, default="")
