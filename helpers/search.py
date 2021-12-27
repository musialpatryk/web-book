from authors.models import Author
from books.models import Book


def remove_duplicates(items):
    items = sorted(items, key=lambda x: x.id)
    for index, item in enumerate(items):
        if index > 0 and item.id == items[index - 1].id:
            items.pop(index)
    return items


def books_full_search(text):
    books_by_title = Book.objects.filter(title__icontains=text, status='A')
    books_by_description = Book.objects.filter(description__icontains=text, status='A')

    results = [
        *books_by_title,
        *books_by_description
    ]

    return remove_duplicates(results)

def authors_full_search(text):
    authors_by_name = Author.objects.filter(name__icontains=text, status='A')
    authors_by_description = Author.objects.filter(description__icontains=text, status='A')

    results = [
        *authors_by_name,
        *authors_by_description
    ]

    return remove_duplicates(results)