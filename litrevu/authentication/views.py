from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm, SignupForm
from authentication.models import User
from authentication.forms import FollowForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User
from .forms import FollowForm


def logout_user(request):
    logout(request)
    return redirect('login')

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
                return redirect('flux')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentication/connection.html', context={'form': form, 'message': message})

def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('flux')
    return render(request, 'authentication/inscription.html', context={'form':form})

@login_required
def follow_view(request):
    user = request.user
    following = user.follows.all()
    followers = user.followers.all()

    form = FollowForm(request.POST or None)
    message = ''

    if request.method == 'POST':
        if 'follow' in request.POST:
            form = FollowForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                try:
                    user_to_follow = User.objects.get(username=username)
                    if user_to_follow == user:
                        message = 'Vous ne pouvez pas vous suivre vous-même.'
                    elif user_to_follow in user.follows.all():
                        message = 'Vous suivez déjà cet utilisateur.'
                    else:
                        user.follows.add(user_to_follow)
                except User.DoesNotExist:
                    message = 'Utilisateur inconnu.'

        elif 'unfollow' in request.POST:
            user_to_unfollow_id = request.POST.get('unfollow')
            user_to_unfollow = get_object_or_404(User, id=user_to_unfollow_id)
            user.follows.remove(user_to_unfollow)

    context = {
        'followers' :followers,
        'following': following,
        'form': form,
        'message': message,
    }

    return render(request, 'authentication/follow.html', context)
