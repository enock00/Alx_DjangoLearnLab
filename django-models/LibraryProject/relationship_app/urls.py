from django.urls import path
from . import views
from .views import LibraryDetailView, CustomLogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
