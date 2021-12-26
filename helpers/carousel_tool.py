from books.models import Book
import random


def get_context(book_list, count=3):
    context = []
    for i in range (count):
        context.append(book_list[i])
    return context

def get_random_context(book_list, count=3):
    context = []
    counter = 0
    while counter < count:
        book = random.choice(book_list)
        if book not in context:
            context.append(book)
            counter += 1
    return context

def get_most_rated_books():
    most_rated_query = "select b.id, count(br.id) as reviews_review from books_book b left join reviews_review br on b.id = br.book_id where b.status='A'group by b.id order by reviews_review desc"
    books = []
    for p in Book.objects.raw(most_rated_query):
        books.append(p)
    return books