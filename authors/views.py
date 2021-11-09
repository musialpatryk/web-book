from django.shortcuts import render
from .models import Author


def book_list(request):
    return render(request, 'authors_list.html', {'authors': Author.objects.all()})


def book_details(request, id):
    book = Book.objects.get(id=id)
    # if null === book:
    return render(request, 'books/book_details.html', {'book': book})

