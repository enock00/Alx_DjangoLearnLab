from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/update/<int:pk>/', BookRetrieveUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
]
