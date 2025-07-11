"""
Models for the Accounts app of Soly - Live Streaming Platform.

Defines the custom user model for the platform, supporting streamer-specific fields and profile customization.

Workflows:
- User model extends Django's AbstractUser, allowing for authentication and profile management.
- Extra fields (display_name, bio, images, is_streamer) support streamer and viewer roles.

Layman explanation:
- This file describes what information is stored for each user, including their name, bio, images, and whether they are a streamer.
- The model is used for login, registration, and profile features.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model for Soly platform.
    - Inherits all standard fields (username, email, password, etc.)
    - Adds extra fields for streamer profiles and platform features.
    """
    display_name = models.CharField(max_length=50, blank=True)  # Public display name for profile
    bio = models.TextField(max_length=500, blank=True)  # Short bio for user profile
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # Profile picture
    banner_image = models.ImageField(upload_to='banner_images/', blank=True, null=True)  # Banner image for profile
    is_streamer = models.BooleanField(default=False)  # True if user is a streamer
    # Add more fields as needed for your platform (e.g., social links, preferences)
    pass
