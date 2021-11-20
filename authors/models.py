from books.models import *
from books.models import AbstractEntity


class Author(AbstractEntity):
    name = models.CharField(max_length=30, default="None")
    genre = models.ManyToManyField("books.Genre", related_name="genre")
    books = models.ManyToManyField("books.Book", related_name="books")
    surname = models.CharField(max_length=30, default="")
    description = models.TextField(default="")
    birthDate = models.DateField()
    rating = models.FloatField()