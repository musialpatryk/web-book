from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from helpers.search import books_full_search, authors_full_search
from reviews.models import Review
from .forms.request_form import BookRequestForm
from .forms.requests_list_form import RequestListForm
from .models import Genre
from django.core.paginator import Paginator
from reviews.forms.review_form import ReviewForm
from authors.models import Author
from general import mailing
from .models import Book
from accounts.decorators import allowed_users, admin_only
from accounts.models import get_users
from django.contrib import messages
from helpers.image_validator import validate_image


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
    try:
        book = Book.objects.get(slug=slug, status = 'A')
    except:
        raise Http404()

    display_reviews = Review.objects.filter(status=Review.STATUS_ACCEPTED, book=book).order_by('-vote')

    form = ReviewForm()
    return render(request, 'books/book_details.html', {'book': book, 'form': form, 'display_reviews': display_reviews})


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def book_create(request):
    if request.method == 'POST':
        book_data = request.POST

        author = Author.objects.get(pk=int(book_data['author']))
        genre = Genre.objects.get(pk=int(book_data['genre']))
        if not validate_image(request.FILES['image']):
            messages.success(request, "Zły format obrazka, spróbuj ponownie")
            return HttpResponseRedirect('/')

        new_book = Book.objects.create_book(
            book_data['title'],
            book_data['description'],
            author,
            genre,
            book_data['publishDate'],
            request.FILES['image']
        )

        new_book.save()

        recipients = get_users('admin')
        mailing.send_mails('New Book Added', 'Hi, New item added to your request list \nhttp://127.0.0.1:8000/books/requests/', recipients)

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
        book_status_change_message(request)

    recipients = get_users('viewer')
    mailing.send_mails('New Book has been added', 'Hi, Book: ' + book.title + ' was approved. Go to BookWeb and check it now \nhttp://127.0.0.1:8000/books/', recipients)

    return HttpResponseRedirect(reverse('books:requests'))


@login_required(login_url='accounts:login')
@admin_only
def book_reject(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        book = Book.objects.get(pk=book_id)
        book.status = 'R'
        book.save()
        book_status_change_message(request)

    return HttpResponseRedirect(reverse('books:requests'))


def book_status_change_message(request):
    messages.success(request, 'Pomyslnie zmieniono status ksiazki')


@login_required(login_url='accounts:login')
@admin_only
def book_delete(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
        messages.success(request, 'Pomyslnie usunieto ksiazke')
        return HttpResponseRedirect("/books/")


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def search_book(request):
    search_text = request.GET.get("search")

    if search_text is None:
        return render(request, 'books/book_not_found.html', {'name': '""'})

    books = books_full_search(search_text)
    authors = authors_full_search(search_text)

    if len(books) == 0 and len(authors) == 0:
        return render(request, 'books/book_not_found.html', {'name': search_text})

    return render(request, 'searched_items.html', {'books': books, 'authors': authors})
