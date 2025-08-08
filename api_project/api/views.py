from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    """
Book API Views
--------------
All endpoints require Token Authentication.

- Obtain a token via POST /api/token/ with 'username' and 'password'
- Include the token in requests as:
    Authorization: Token <"498fc646ea9d60ed6d2dc4d22e974ffb5cf88d90">
"""