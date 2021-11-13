from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Author

@login_required(login_url='accounts:login')
def author_list(request):
    return render(request, 'authors/authors_list.html', {'authors': Author.objects.all()})

@login_required(login_url='accounts:login')
def author_details(request, slug):
    author = Author.objects.get(slug=slug)
    # if null === book:
    return render(request, 'authors/authors_details.html', {'author': author})

