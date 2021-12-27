from django.core.validators import FileExtensionValidator
from django.utils.text import slugify

from books.models import AbstractEntity
from books.models import models


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
        author_slug = slugify(slug)
        potential_slug_duplicate_len = len(self.filter(slug=author_slug))
        if potential_slug_duplicate_len > 0:
            author_slug += '-' + str(potential_slug_duplicate_len)

        author = self.create(
            name=name,
            description=description,
            birthDate=birthDate,
            rating=0,
            slug=author_slug,
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
        default='author_images/default_author_1.jpg',
        upload_to='author_images',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]
    )

    def __str__(self):
        return self.name

    def snippet(self):
        return self.description[:50] + '...'
