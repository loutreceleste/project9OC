from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from authentication.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")

class SignupForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class FollowForm(forms.Form):
    username = forms.CharField(max_length=150)