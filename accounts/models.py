from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from accounts.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Enter Username...',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Enter Email...',
            })
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Enter Password...'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Re-enter Password...'})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default='None')
    phone = models.CharField(max_length=50, default='None')
    image = models.ImageField(default='default.png',
                              upload_to='profile_images')

    def __str__(self):
        return f'{self.user.username}-Profile'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']


class AbstractEntity(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    ROLES = (
        ("V", "Viewer"),
        ("E", "Editor"),
        ("A", "Admin"),
    )
    Roles = models.CharField(choices=ROLES, max_length=6)


class Book(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Authors = models.ManyToManyField("Author")
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Genre = models.ManyToManyField("Genre")
    Rating = models.FloatField()
    Pages = models.IntegerField()


class Author(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE, related_name="abstractEntityAccounts")
    Name = models.CharField(max_length=20)
    Genre = models.ManyToManyField("Genre")
    Books = models.ManyToManyField(Book)
    Surname = models.CharField(max_length=20)
    Description = models.TextField()
    BirthDate = models.DateField()
    Rating = models.FloatField()


class Genre(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Title = models.CharField(max_length=30)
    Slug = models.CharField(max_length=30)


class Review(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Vote = models.IntegerField()
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Review = models.CharField(max_length=30)
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
    Status = models.CharField(choices=STATUS, max_length=10)


class Series(models.Model):
    AbstractEntity = models.ForeignKey(AbstractEntity, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Authors = models.ManyToManyField(Author)
    Book = models.ManyToManyField(Book)
    Description = models.TextField()
    Rating = models.FloatField()



