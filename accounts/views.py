from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CreateUserForm
from .decorators import unauthenticated_user


@unauthenticated_user
def signup_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='viewer')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('accounts:login')
    else:
        form = CreateUserForm()
    return render(request, 'accounts/signup.html', {'form': form})


@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')


def user_profile_view(request):
    context = {

    }
    return render(request, 'accounts/user_profile.html', context)


def UpdateUser_profile_view(request):
    context = {

    }
    return render(request, 'accounts/UpdateUser_profile.html', context)