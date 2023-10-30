from django.db import models

class Users(models.Model):
    username = models.fields.CharField(max_length=100)
    password = models.fields.CharField(max_length=100)

