from books.models import AbstractEntity
from books.models import models


class Author(AbstractEntity):
    name = models.CharField(max_length=30, default="None")
    genre = models.ManyToManyField("books.Genre", related_name="genre")
    books = models.ManyToManyField("books.Book", related_name="books")
    surname = models.CharField(max_length=30, default="None")
    description = models.TextField(default="None")
    birthDate = models.DateField()
    rating = models.FloatField(default=5.0)