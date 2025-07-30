from django import forms
from .models import Book
from django.contrib.auth import get_user_model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

User = get_user_model()

class CustomUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'profile_photo', 'password']