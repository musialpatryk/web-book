from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
from general.models import AbstractEntity


class ReviewManager(models.Manager):
    def create_review(
            self,
            vote,
            review,
            book,
            user
    ):
        return self.create(
            vote = vote,
            review = review,
            book = book,
            user = user
        )


class Review(AbstractEntity):
    STATUS_PENDING = 0
    STATUS_REJECTED = 1
    STATUS_ACCEPTED = 2
    objects = ReviewManager()

    vote = models.IntegerField(default=0,
                               validators=[
                                   MaxValueValidator(5),
                                   MinValueValidator(0),
                               ])
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=30, default="None")
    status = models.IntegerField(default=STATUS_PENDING)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)


