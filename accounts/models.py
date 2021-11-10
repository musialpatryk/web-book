from django.db import models

# Create your models here.


class AbstractEntity(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Username = models.CharField()
    Password = models.CharField()
    ROLES = (
        ("V", "Viewer"),
        ("E", "Editor"),
        ("A", "Admin"),
    )
    Roles = models.CharField(choices=ROLES)


class Book(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Authors = models.ManyToManyField(Author)
    Title = models.CharField()
    Description = models.TextField()
    Genre = models.ManyToManyField(Genre)
    Rating = models.FloatField()
    Pages = models.IntegerField()


class Author(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Name = models.CharField()
    Genre = models.ManyToManyField(Genre)
    Books = models.ManyToManyField(Book)
    Surname = models.CharField()
    Description = models.TextField()
    BirthDate = models.DateField()
    Rating = models.FloatField()


class Genre(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Title = models.CharField()
    Slug = models.CharField()


class Review(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Vote = models.IntegerField()
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Review = models.CharField()
    Upvotes = models.IntegerField()
    Downvotes = models.IntegerField()


class FavoriteBooks(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)


# Optional

class BookRequest(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    STATUS = (
        ("P", "Pending"),
        ("A", "Accepted"),
        ("R", "Rejected")
    )
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Status = models.CharField(choices=STATUS)


class Series(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Name = models.CharField()
    Authors = models.ManyToManyField(Author)
    Book = models.ManyToManyField(Book)
    Description = models.TextField()
    Rating = models.FloatField()



