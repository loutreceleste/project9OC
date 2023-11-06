from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Le nom d'utilisateur est obligatoire.")
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser):
    username = models.fields.CharField(max_length=100, unique=True)
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')

    objects = UserManager()

    USERNAME_FIELD = "username"

