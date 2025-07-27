from django.db import models

# Create your models here.
from django.db import models

# OneToOne: Profile for each Author
class Author(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField()

# ForeignKey: Book belongs to one Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# ManyToMany: Book can have multiple categories, and category can include many books
class Category(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)
