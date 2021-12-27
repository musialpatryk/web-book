from books.models import Book
from authors.models import Author
from helpers.random_photo import get_random_photo

for entry in Book.objects.all():
    entry.image = get_random_photo('book_images/')
    entry.save()

for entry in Author.objects.all():
    entry.image = get_random_photo('author_images/', False)
    entry.save()