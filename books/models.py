from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    publishDate = models.DateTimeField(auto_now_add=True)

    # author

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50] + '...'
