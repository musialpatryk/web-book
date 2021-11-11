from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def book_list(request):
    books = Book.objects.all().order_by('publishDate')
    return render(request, 'book_list.html', {'books': books})


@login_required(login_url='accounts:login')
def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'book_details.html', {'book': book})


@login_required(login_url="/accounts/login/")
def book_create(request):
    return render(request, 'book_create.html')
