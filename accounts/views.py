from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CreateUserForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                # ToBeDeleted
                # user = form.save()
                #log the user in
                # login(request, user)
                return redirect('accounts:login')
        else:
            form = CreateUserForm()
        return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR Password is incorrect')
            # ToBeDeleted
            # form = AuthenticationForm(data=request.POST)
            # if form.is_valid():
            #     #log in user
            #     user = form.get_user()
            #     login(request, user)
            #     return redirect('/')
        # else:
            # form = AuthenticationForm()
            form = {}
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
