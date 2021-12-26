from django.core.validators import FileExtensionValidator

from books.models import AbstractEntity
from books.models import models
from helpers.random_photo import get_random_photo


class AuthorManager(models.Manager):
    def create_author(
            self,
            name,
            genre,
            description,
            birthDate,
            slug,
            image
    ):

        author = self.create(
            name=name,
            description=description,
            birthDate=birthDate,
            rating=0,
            slug=slug,
            image=image,
        )
        author.genre.set([genre])
        return author


class Author(AbstractEntity):
    objects = AuthorManager()

    STATUS = (
        ("P", "Pending"),
        ("A", "Accepted"),
        ("R", "Rejected")
    )
    name = models.CharField(max_length=30, default="None")
    genre = models.ManyToManyField("books.Genre", related_name="genre")
    description = models.TextField(default="None")
    birthDate = models.DateField()
    slug = models.SlugField(default="None")
    rating = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS, max_length=10, default="P")
    image = models.ImageField(
        default='default_author_1.jpg',
        upload_to='author_images',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]
    )

    def __str__(self):
        return self.name

    def snippet(self):
        return self.description[:50] + '...'
