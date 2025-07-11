"""
accounts/serializers.py

This module defines serializers for the User model, which are used to convert complex data types
(like Django models) into native Python datatypes that can then be easily rendered into JSON, XML, or other content types.
Serializers also handle validation and creation of User instances from incoming API data.
"""

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # The password field is write-only, meaning it will not be returned in API responses.
    # This helps keep user passwords secure and hidden from clients.
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        # These fields are exposed via the API for user objects.
        # Some fields are read-only and cannot be changed via API (e.g., id, is_staff).
        fields = [
            'id', 'username', 'email', 'display_name', 'bio', 'profile_image', 'banner_image',
            'is_streamer', 'is_staff', 'is_active', 'date_joined', 'last_login', 'password'
        ]
        read_only_fields = ['id', 'is_staff', 'is_active', 'date_joined', 'last_login']

    def create(self, validated_data):
        """
        Creates a new User instance from validated data.
        If a password is provided, it is securely hashed before saving.
        This ensures that raw passwords are never stored in the database.
        """
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)  # Hashes the password
            user.save()
        return user
