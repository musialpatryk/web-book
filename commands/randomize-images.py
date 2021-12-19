from books.models import Book
from helpers.random_photo import get_random_photo

for entry in Book.objects.all() :
    entry.image = get_random_photo()
    entry.save()