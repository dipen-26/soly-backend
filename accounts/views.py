"""
accounts/views.py

This module defines views for user-related API endpoints using Django REST Framework's ModelViewSet.
Views handle incoming HTTP requests, interact with models and serializers, and return responses.
"""

from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for User objects via REST API.
    Only authenticated users can access these endpoints by default.
    You can extend this class to add custom registration, profile update, or streamer onboarding logic.
    """
    queryset = User.objects.all()  # All users are available for API operations
    serializer_class = UserSerializer  # Uses the UserSerializer for input/output
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can access
    # Custom logic for registration, user profile update, or streamer onboarding can be added here

# Note: The 'render' import is unused here, but could be used for rendering HTML templates if needed.
# Views are the main entry point for handling API requests related to users.
