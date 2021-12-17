from django.contrib import admin
from .models import Book, Genre, FavoriteBooks, Series

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(FavoriteBooks)
admin.site.register(Series)
