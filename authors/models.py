from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    description = models.TextField()
    birthDate = models.DateField()
