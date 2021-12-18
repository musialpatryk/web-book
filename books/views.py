from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from .forms.requests_list_form import RequestListForm
from .models import Genre
from books.forms.request_form import BookRequestForm
from django.core.paginator import Paginator

from reviews.forms.review_form import ReviewForm
from authors.models import Author
from .models import Book
from accounts.decorators import allowed_users, admin_only


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def book_list(request):
    p = Paginator(Book.objects.filter(status='A').order_by('publishDate'), 10)
    page = request.GET.get('page')
    books = p.get_page(page)
    return render(request, 'books/book_list.html', {'books': books})


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    form = ReviewForm()
    return render(request, 'books/book_details.html', {'book': book, 'form': form})


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
            genre,
            book_data['publishDate'],
            request.FILES['image']
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
    p = Paginator(forms, 10)
    page = request.GET.get('page')
    forms = p.get_page(page)

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


@login_required(login_url='accounts:login')
@admin_only
def book_delete(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()

        return HttpResponseRedirect("/books/")


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def search_book(request):
    book_get = request.GET
    name = book_get.get("title")
    if Book.objects.filter(title__icontains=name).exists():
        book = Book.objects.filter(title__icontains=name)
        author = Author.objects.filter(book__title__icontains=name)
        return render(request, 'books/book_search.html', {'books': book, 'authors': author})
    elif Book.objects.filter(authors__name__icontains=name).exists():
        book = Book.objects.filter(authors__name__icontains=name)
        author = Author.objects.filter(name__icontains=name)
        return render(request, 'books/book_search.html', {'books': book, 'authors': author})
    else:
        return render(request, 'books/book_not_found.html', {'name': name})