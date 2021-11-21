from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms.requests_list_form import RequestListForm
from .models import Book, Genre
from accounts.decorators import allowed_users, admin_only
from books.forms.request_form import BookRequestForm
from authors.models import Author


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def book_list(request):
    books = Book.objects.filter(status='A').order_by('publishDate')
    return render(request, 'books/book_list.html', {'books': books})


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_details.html', {'book': book})


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def book_create(request):
    if request.method == 'POST':
        book_data = request.POST

        author = Author.objects.get(pk=int(book_data['author']))
        genre = Genre.objects.get(pk=int(book_data['genre']))
        new_book = Book.objects.create_book(
            book_data['title'],
            book_data['description'],
            author,
            genre
        )
        new_book.save()

        return HttpResponseRedirect('/')

    author_options = []
    for author in Author.objects.all():
        author_options.append((author.id, author.__str__()))

    genre_options = []
    for genre in Genre.objects.all():
        genre_options.append((genre.id, genre.__str__()))

    form = BookRequestForm(authors=author_options, genre=genre_options)
    return render(request, 'books/book_create.html', {'form': form})


@login_required(login_url='accounts:login')
@admin_only
def book_requests(request):
    forms = []
    for book in Book.objects.filter(status='P').order_by('-publishDate'):
        forms.append(RequestListForm(book=book))

    return render(request, 'books/book_requests.html', {'forms': forms})


@login_required(login_url='accounts:login')
@admin_only
def book_accept(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        book = Book.objects.get(pk=book_id)
        book.status = 'A'
        book.save()

    return HttpResponseRedirect(reverse('books:requests'))


@login_required(login_url='accounts:login')
@admin_only
def book_reject(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        book = Book.objects.get(pk=book_id)
        book.status = 'R'
        book.save()

    return HttpResponseRedirect(reverse('books:requests'))
