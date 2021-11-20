from general.models import AbstractEntity
from django.db import models
from authors.models import Author


class Genre(AbstractEntity):
    Title = models.CharField(max_length=30, default="None")
    Slug = models.CharField(max_length=30, default="None")


class Book(AbstractEntity):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=50, default="None")
    description = models.TextField(default="None")
    genre = models.ManyToManyField(Genre)
    rating = models.FloatField(5.0)
    pages = models.IntegerField(default=1)

    # author

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50] + '...'


class FavoriteBooks(AbstractEntity):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)


class Review(AbstractEntity):
    vote = models.IntegerField()
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    review = models.CharField(max_length=30, default="None")
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()


# Optional

class BookRequest(Book):
    STATUS = (
        ("P", "Pending"),
        ("A", "Accepted"),
        ("R", "Rejected")
    )
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=10, default="None")


class Series(AbstractEntity):
    name = models.CharField(max_length=30, default="None")
    authors = models.ManyToManyField(Author)
    book = models.ManyToManyField(Book)
    description = models.TextField(default="None")
    rating = models.FloatField()

