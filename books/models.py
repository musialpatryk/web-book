from authors.models import Author
from accounts.models import *
from general.models import AbstractEntity


class Genre(AbstractEntity):
    Title = models.CharField(max_length=30, default="None")
    Slug = models.CharField(max_length=30, default="None")


class Book(AbstractEntity):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=50, default="None")
    description = models.TextField(default="None")
    genre = models.ManyToManyField(Genre)
    rating = models.FloatField()
    pages = models.IntegerField()

    # author

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50] + '...'


class FavoriteBooks(AbstractEntity):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Optional

class BookRequest(Book):
    STATUS = (
        ("P", "Pending"),
        ("A", "Accepted"),
        ("R", "Rejected")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=10, default="None")


class Series(AbstractEntity):
    name = models.CharField(max_length=30, default="None")
    authors = models.ManyToManyField(Author)
    book = models.ManyToManyField(Book)
    description = models.TextField(default="None")
    rating = models.FloatField()

