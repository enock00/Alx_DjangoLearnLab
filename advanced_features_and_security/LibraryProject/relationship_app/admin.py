from django.contrib import admin
from bookshelf.models import CustomUser
from .models import Book, Library, Author, UserProfile

admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Author)
admin.site.register(UserProfile)
