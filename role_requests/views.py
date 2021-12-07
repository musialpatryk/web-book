from django.shortcuts import render
from .models import RoleRequest
from django.http import HttpResponseRedirect
from .forms.role_request_form import RoleRequestForm

# Create your views here.

def role_request_list():
    role_requests = RoleRequest.objects.filter(status=RoleRequest.STATUS_PENDING)
    return render(request, 'role_requests/role_request_list.html', {'role_requests': role_requests})


def role_request_create(request):
    if request.method == 'POST':
        role_request_data = request.POST
        role_request = RoleRequest.objects.create_role_request(
            role_request_data['message']
        )
        role_request.save()
        return HttpResponseRedirect('/')

    form = RoleRequestForm()
    return render(request, 'role_requests/role_request_create.html', {'form': form})