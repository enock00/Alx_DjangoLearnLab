from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
  
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access

class BookDetailView(generics.RetrieveAPIView):
   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access


class BookCreateView(generics.CreateAPIView):
   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
       
        serializer.is_valid(raise_exception=True)
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
  
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
       
        serializer.is_valid(raise_exception=True)
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
