from django.urls import path
from .views import list_books, LibraryDetailView
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('list_books')),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]