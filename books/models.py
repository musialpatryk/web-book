from django.utils.text import slugify

from general.models import AbstractEntity
from django.db import models
from authors.models import Author
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

from helpers.random_photo import get_random_photo


class Genre(AbstractEntity):
    genreName = models.CharField(max_length=30, default="None")
    slug = models.CharField(max_length=30, default="None")

    def __str__(self):
        return self.genreName


class BookManager(models.Manager):
    def create_book(
            self,
            title,
            description,
            author,
            genre,
            publishDate,
            image
    ):
        book_slug = slugify(title)
        potential_slug_duplicate_len = len(self.filter(slug=book_slug))
        if potential_slug_duplicate_len > 0:
           book_slug += '-' + str(potential_slug_duplicate_len)

        book = self.create(
            title=title,
            description=description,
            pages=2,
            rating=0,
            slug=book_slug,
            publishDate=publishDate,
            image=image
        )
        book.authors.set([author])
        book.genre.set([genre])
        return book


class Book(AbstractEntity):
    objects = BookManager()

    STATUS = (
        ("P", "Pending"),
        ("A", "Accepted"),
        ("R", "Rejected")
    )
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=100, default="None")
    description = models.TextField(default="None")
    genre = models.ManyToManyField(Genre)
    rating = models.IntegerField(default=0)
    pages = models.IntegerField(default=None)
    slug = models.SlugField(max_length=100)
    publishDate = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=10, default="P")
    image = models.ImageField(
        default='book_images/default_book_1.jpg',
        upload_to='book_images',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]
    )

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50] + '...'


class FavoriteBooks(AbstractEntity):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Optional


class Series(AbstractEntity):
    name = models.CharField(max_length=30, default="None")
    authors = models.ManyToManyField(Author)
    book = models.ManyToManyField(Book)
    description = models.TextField(default="None")
    rating = models.FloatField(default=None)

