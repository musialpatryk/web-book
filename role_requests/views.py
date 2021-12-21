from django.shortcuts import render
from .models import RoleRequest
from django.http import HttpResponseRedirect
from .forms.role_request_form import RoleRequestForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from accounts.decorators import allowed_users, admin_only
from django.contrib.auth.decorators import login_required

# Create your views here.
@admin_only
@login_required(login_url='accounts:login')
def role_request_list(request):
    role_requests = RoleRequest.objects.filter(status=RoleRequest.STATUS_PENDING)
    return render(request, 'role_requests/role_request_list.html', {'role_requests': role_requests})


def role_request_create(request):
    if request.method == 'POST':
        try:
            role_request = RoleRequest.objects.get(user=request.user, status = RoleRequest.STATUS_PENDING)
        except:
            role_request = None

        if role_request is not None:
            messages.success(request, "Mozna zlozyc tylko jedno podanie na moderatora na raz")
            return HttpResponseRedirect('/')

        for group in request.user.groups.all():
            if group.name == "admin":
                messages.success(request, "Nie trzeba przyznawać uprawnień")
                return HttpResponseRedirect('/')

        return HttpResponseRedirect('/')

        role_request = RoleRequest.objects.create_role_request(
            request.POST['message'],
            request.user
        )
        role_request.save()
        messages.success(request, "Pomyslnie zlozono wniosek o nadanie uprawnien moderatora")
        return HttpResponseRedirect('/')

    form = RoleRequestForm()
    return render(request, 'role_requests/role_request_create.html', {'form': form})

def accept_role_request(request):
    return role_request_change_status(request, RoleRequest.STATUS_ACCEPTED)

def reject_role_request(request):
    return role_request_change_status(request, RoleRequest.STATUS_REJECTED)

@admin_only
@login_required(login_url='accounts:login')
def role_request_change_status(request, status):
    if request.method != 'POST':
        return HttpResponseRedirect('/')

    if status != RoleRequest.STATUS_REJECTED and status != RoleRequest.STATUS_PENDING and status != RoleRequest.STATUS_ACCEPTED:
        return HttpResponseRedirect('/')

    role_request = RoleRequest.objects.get(pk=request.POST['role_request_id'])

    role_request.status = status
    role_request.save()
    if role_request.status == RoleRequest.STATUS_ACCEPTED:
        group = Group.objects.get(name='admin')
        role_request.user.groups.add(group)

    messages.success(request, "Pomyslnie zmieniono status podania")
    return HttpResponseRedirect('/')
