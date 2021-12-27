from authors.models import Author
Author.objects.all().delete()

from books.models import Book
Book.objects.all().delete()

from books.models import Genre
Genre.objects.all().delete()

from django.contrib.auth.models import User, Group
User.objects.all().delete()
Group.objects.all().delete()

# Currently is not working.
# from allauth.account.apps import AppConfig
# AppConfig.objects.all().delete()