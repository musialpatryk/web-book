from books.models import Book
from reviews.models import Review
from django.db.models import Avg


def recalculate_book_rating(book):
    book_rating = Review\
        .objects\
        .filter(book = book, status = Review.STATUS_ACCEPTED)\
        .aggregate(rating = Avg('vote'))

    book.rating = book_rating['rating']
    book.save()


def recalculate_author_rating(authors):
    for author in authors:
        author_rating = Book\
            .objects\
            .filter(authors = author)\
            .aggregate(rating = Avg('rating'))

        author.rating = author_rating['rating']
        author.save()