from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

from relationship_app.models import Author, Book, Library

# Query 1: All books by a specific author
def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")

# Query 2: List all books in a library
def get_books_in_library(library_name):
    books = Book.objects.filter(library__name=library_name)
    print(f"Books in {library_name} library:")
    for book in books:
        print(f"- {book.title}")

# Sample usage
if __name__ == "__main__":
    get_books_by_author("Langat")
    get_books_in_library("Downtown Library")

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)