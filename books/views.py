from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from authors.models import Author
from .models import Book
from accounts.decorators import allowed_users, unauthenticated_user, admin_only
from django.db.models import Value as V
from django.db.models.functions import Concat


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
    date = name.split(" ")
    if Book.objects.filter(title__contains=name).exists():
        book = Book.objects.filter(title__contains=name)
        return render(request, 'books/book_search.html', {'books': book})
    elif Book.objects.filter(authors__name__contains=name).exists():
        book = Book.objects.filter(authors__name__contains=name)
        return render(request, 'books/book_search.html', {'books': book})
    elif Book.objects.filter(authors__surname__contains=name).exists():
        book = Book.objects.filter(authors__surname__contains=name)
        return render(request, 'books/book_search.html', {'books': book})
    elif Author.objects.annotate(full_name=Concat('name', V(' '), 'surname')).filter(full_name__icontains=name):
        book = Book.objects.filter(authors__name__contains=date[0]).filter(authors__surname=date[1])
        return render(request, 'books/book_search.html', {'books': book})
    else:
        return render(request, 'books/book_search.html')