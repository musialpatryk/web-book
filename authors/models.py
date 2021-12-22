from django.core.validators import FileExtensionValidator

from books.models import AbstractEntity
from books.models import models
from helpers.random_photo import get_random_photo


class Author(AbstractEntity):
    name = models.CharField(max_length=30, default="None")
    genre = models.ManyToManyField("books.Genre", related_name="genre")
    description = models.TextField(default="None")
    birthDate = models.DateField()
    slug = models.SlugField(default="None")
    rating = models.IntegerField(default=0)
    image = models.ImageField(
        default='default_author_1.jpg',
        upload_to='author_images',
        validators=[FileExtensionValidator(allowed_extensions=['png'])]
    )

    def __str__(self):
        return self.name
