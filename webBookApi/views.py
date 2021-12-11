import random

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from books.models import Book


@login_required(login_url='accounts:login')
def home(request):
    books_today = Book.objects.all().order_by("?")
    today_1 = random.choice(books_today)
    today_2 = random.choice(books_today)
    today_3 = random.choice(books_today)
    today_4 = random.choice(books_today)
    today_5 = random.choice(books_today)

    book_for_you = Book.objects.all().order_by("?")
    for_you_1 = random.choice(book_for_you)
    for_you_2 = random.choice(book_for_you)
    for_you_3 = random.choice(book_for_you)

    book_raw = []
    for p in Book.objects.raw('select b.id, count(br.id) as books_review from books_book b left join books_review br on b.id = br.book_id group by b.id order by books_review desc'):
        book_raw.append(p)

    most_rated_1 = book_raw[0]
    most_rated_2 = book_raw[1]
    most_rated_3 = book_raw[2]

    books_top = Book.objects.all().order_by('-rating')
    top1 = books_top[0]
    top2 = books_top[1]
    top3 = books_top[2]

    book_new = Book.objects.all().order_by('-publishDate')
    new1 = book_new[0]
    new2 = book_new[1]
    new3 = book_new[2]

    context = {'today_1': today_1, 'today_2': today_2, 'today_3': today_3, 'today_4': today_4, 'today_5': today_5,
               'for_you_1': for_you_1, 'for_you_2': for_you_2, 'for_you_3': for_you_3,
               'top1': top1, 'top2': top2, 'top3': top3,
               'new1': new1, 'new2': new2, 'new3': new3,
               'most_rated_1': most_rated_1, 'most_rated_2': most_rated_2, 'most_rated_3': most_rated_3,
               }

    return render(request, 'homepage.html', context)


@login_required(login_url='accounts:login')
def about(request):
    return render(request, 'about.html')


def error_404(request, *args, **argv):
    return render(request, '404.html', status=404)


def error_500(request, *args, **argv):
    return render(request, '500.html', status=404)



