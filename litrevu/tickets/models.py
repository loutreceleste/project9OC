from django.conf import settings
from django.db import models
from django_resized import ResizedImageField

class CreateTicket(models.Model):
    book_title = models.fields.CharField(max_length=128, default="")
    book_description = models.fields.CharField(max_length=2048, default="")
    book_image = ResizedImageField(size=[500, 300], upload_to='main', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default="")
