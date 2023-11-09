from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from tickets.models import CreateTicket


class CreateReviewWithTicket(models.Model):

    ticket = models.ForeignKey(CreateTicket, on_delete=models.CASCADE, related_name='reviews')
    headline = models.CharField(max_length=128)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
