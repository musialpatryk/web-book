from authors.models import Author
Author.objects.all().delete()

from books.models import Book
Book.objects.all().delete()

from django.contrib.auth.models import User, Group
User.objects.all().delete()
Group.objects.all().delete()