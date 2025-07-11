"""
accounts/urls.py

This module defines URL routes for the accounts app, mapping API endpoints to their corresponding views.
It uses Django REST Framework's router for user CRUD operations and explicit paths for registration and login.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .auth_views import RegisterView, LoginView

# Router automatically generates RESTful routes for UserViewSet (list, create, retrieve, update, delete)
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all user CRUD endpoints
    path('register/', RegisterView.as_view(), name='register'),  # User registration endpoint
    path('login/', LoginView.as_view(), name='login'),  # User login endpoint
]

# This file connects HTTP requests to the correct view logic for user management and authentication.
