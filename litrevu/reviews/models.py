from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_resized import ResizedImageField
from django.conf import settings

class CreateTicketForReview(models.Model):
    book_title = models.fields.CharField(max_length=100, default="")
    book_description = models.fields.CharField(max_length=100, default="")
    book_image = ResizedImageField(size=[500, 300], upload_to='main', blank=True, default=None)

class CreateReviewWithTicket(models.Model):
    ticket = models.ForeignKey(to=CreateTicketForReview, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
