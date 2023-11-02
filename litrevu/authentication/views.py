from django.shortcuts import render
from django.contrib.auth import authenticate, login
from authentication.forms import LoginForm


def connection(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentication/connection.html', context={'form': form, 'message': message})


def inscription(request):
    return render(request, 'authentication/inscription.html')