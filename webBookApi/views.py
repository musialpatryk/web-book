from django.shortcuts import render


def home(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')

def error_404(request, *args, **argv):
    return render(request, '404.html', status=404)


def error_500(request, *args, **argv):
    return render(request, '500.html', status=404)

