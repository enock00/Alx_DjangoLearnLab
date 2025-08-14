from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

app_name = 'blog'

urlpatterns = [
    # Home & user management
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # CRUD paths for blog posts
    path('posts/', PostListView.as_view(), name='post-list'),              # List all posts
    path('posts/new/', PostCreateView.as_view(), name='post-create'),      # Create a new post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # View post details
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete a post
]

