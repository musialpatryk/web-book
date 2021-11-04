from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def book_list(request):
    books = Book.objects.all().order_by('publishDate')
    return render(request, 'books/book_list.html', {'books': books})


def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_details.html', {'book': book})


@login_required(login_url="/accounts/login/")
def book_create(request):
    return render(request, 'books/book_create.html')
