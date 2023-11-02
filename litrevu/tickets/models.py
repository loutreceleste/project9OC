from django.db import models

class CreateTicket(models.Model):
    book_title = models.fields.CharField(max_length=100, default="")
    book_description = models.fields.CharField(max_length=100, default="")
    book_image = models.ImageField()
    pass
class ModifyTicket(models.Model):
    book_title = models.fields.CharField(max_length=100, default="")
    book_description = models.fields.CharField(max_length=100, default="")
    book_image = models.ImageField()
    pass