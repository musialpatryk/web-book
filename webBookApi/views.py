from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def home(request):
    return render(request, 'homepage.html')


@login_required(login_url='accounts:login')
def about(request):
    return render(request, 'about.html')


def error_404(request, *args, **argv):
    return render(request, '404.html', status=404)


def error_500(request, *args, **argv):
    return render(request, '500.html', status=404)

