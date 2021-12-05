from books.models import AbstractEntity
from books.models import models


class Author(AbstractEntity):
    name = models.CharField(max_length=30, default="None")
    genre = models.ManyToManyField("books.Genre", related_name="genre")
    description = models.TextField(default="None")
    birthDate = models.DateField()
    slug = models.SlugField(default="None")
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name
