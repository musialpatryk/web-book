from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from books.models import Book
from helpers.carousel_tool import get_most_rated_books, get_random_context, get_context


@login_required(login_url='accounts:login')
def home(request):
    books_today = Book.objects.filter(status='A').order_by("?")
    book_for_you = Book.objects.filter(status='A').order_by("?")
    most_rated_books = get_most_rated_books()
    books_top = Book.objects.filter(status='A').order_by('-rating')
    book_new = Book.objects.filter(status='A').order_by('-publishDate')

    context = {
        'today_list': get_random_context(books_today, 5),
        'random_list': get_random_context(book_for_you),
        'most_rated_list': get_context(most_rated_books),
        'top_books_list': get_context(books_top),
        'new_books_list': get_context(book_new)
    }

    return render(request, 'homepage.html', context)


@login_required(login_url='accounts:login')
def about(request):
    return render(request, 'about.html')


def error_404(request, *args, **argv):
    return render(request, '404.html', status=404)


def error_500(request, *args, **argv):
    return render(request, '500.html', status=404)



