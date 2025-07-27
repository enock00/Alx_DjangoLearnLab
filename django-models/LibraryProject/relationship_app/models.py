from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Profile: One-to-One with Author
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return f"{self.author.name}'s Profile"

# Library model
class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Librarian: One-to-One with Library
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Book: belongs to Author and Library
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

# Category: Many-to-Many with Book
class Category(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name="categories")

    def __str__(self):
        return self.name
