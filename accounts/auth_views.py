"""
accounts/auth_views.py

This module provides authentication-related API views for user registration and login.
It uses Django REST Framework generics and Knox for token-based authentication.
Custom logic (like email verification or ML-based fraud detection) can be added to these views.
"""

from rest_framework import generics, permissions
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    Accepts user data, validates it, and creates a new User instance.
    You can add custom registration logic here, such as sending email verification or enriching user profiles.
    ML/DL stub: This is a good place to add machine learning for fraud detection or profile enrichment.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can register
    # Custom registration logic can be added here

class LoginView(KnoxLoginView):
    """
    API endpoint for user login using Knox token authentication.
    Accepts username and password, authenticates the user, and returns an authentication token.
    ML/DL stub: You can add login anomaly detection or behavioral analytics here for security.
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # AuthTokenSerializer validates the username and password
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)  # Logs the user in (session-based)
        # ML/DL stub: Add login anomaly detection or analytics here
        return super(LoginView, self).post(request, format=None)
