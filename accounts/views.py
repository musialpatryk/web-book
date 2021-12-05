from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='accounts:login')
def user_profile_view(request):
    return render(request, 'accounts/user_profile.html')


@login_required(login_url='accounts:login')
def UpdateUser_profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('accounts:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'accounts/UpdateUser_profile.html', context)
