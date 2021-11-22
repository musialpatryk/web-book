import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Book
# from ..accounts.decorators import allowed_users, unauthenticated_user
from .decorators import allowed_users, admin_only


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def book_list(request):
    books = Book.objects.all().order_by('publishDate')
    return render(request, 'books/book_list.html', {'books': books})


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_details.html', {'book': book})


@login_required(login_url='accounts:login')
@admin_only
def book_create(request):
    return render(request, 'books/book_create.html')


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def search_book(request):
    book_get = request.GET
    name = book_get.get("title")
    if Book.objects.filter(title=name).exists():
        book = Book.objects.filter(title=name)
        return render(request, 'books/book_search.html', {'books': book})
    elif Book.objects.filter(author=name).exists():
        book = Book.objects.filter(author=name)
        return render(request, 'books/book_search.html', {'books': book})
    else:
        book = Book.objects.all()
        return render(request, 'books/book_search.html', {'books': book})

