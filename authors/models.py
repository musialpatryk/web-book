from django.db import models

from accounts.models import *


# Create your models here.


# class Author(models.Model):
#     name = models.CharField(max_length=20)
#     surname = models.CharField(max_length=20)
#     description = models.TextField()
#     birthDate = models.DateField()
#     slug = models.SlugField()


class Author(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE, related_name="abstractEntityAccounts")
    Name = models.CharField(max_length=30)
    Genre = models.ManyToManyField(Genre, related_name="genre")
    Books = models.ManyToManyField(Book, related_name="books")
    Surname = models.CharField(max_length=30)
    Description = models.TextField()
    BirthDate = models.DateField()
    Rating = models.FloatField()