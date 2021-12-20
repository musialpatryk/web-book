from django.shortcuts import render
from .models import RoleRequest
from django.http import HttpResponseRedirect
from .forms.role_request_form import RoleRequestForm
from django.contrib.auth.models import User, Group

# Create your views here.

def role_request_list(request):
    role_requests = RoleRequest.objects.filter(status=RoleRequest.STATUS_PENDING)
    return render(request, 'role_requests/role_request_list.html', {'role_requests': role_requests})


def role_request_create(request):
    if request.method == 'POST':
        try:
            role_request = RoleRequest.objects.get(user=request.user)
        except:
            role_request = None

        if role_request is not None:
            return HttpResponseRedirect('/')
        role_request = RoleRequest.objects.create_role_request(
            request.POST['message'],
            request.user
        )
        role_request.save()
        return HttpResponseRedirect('/')

    form = RoleRequestForm()
    return render(request, 'role_requests/role_request_create.html', {'form': form})

def accept_role_request(request):
    return role_request_change_status(request, RoleRequest.STATUS_ACCEPTED)

def reject_role_request(request):
    return role_request_change_status(request, RoleRequest.STATUS_REJECTED)

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

    return HttpResponseRedirect('/')
