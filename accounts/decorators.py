from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


# Wywołujecie tą metodą z nazwą grupy która jest wymagana do odwiedzenia strony
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                for group in request.user.groups.all():
                    if group.name in allowed_roles:
                        return view_func(request, *args, **kwargs)
            return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.exists():
            for group in request.user.groups.all():
                if group.name == 'admin':
                    return view_func(request, *args, **kwargs)
                if group.name == 'viewer':
                    return redirect('/')
    return wrapper_func
