from authors.models import Author
Author.objects.all().delete()

from books.models import Book
Book.objects.all().delete()