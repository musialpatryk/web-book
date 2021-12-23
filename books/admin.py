from django.contrib import admin
from .models import Book, Genre, FavoriteBooks, Series
from role_requests.models import RoleRequest

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(FavoriteBooks)
admin.site.register(Series)
admin.site.register(RoleRequest)
