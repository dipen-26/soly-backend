"""
accounts/admin.py

This module customizes the Django admin interface for the User model.
It allows administrators to view, search, and filter user accounts efficiently.
"""

from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for User objects.
    - list_display: Shows these fields in the user list view.
    - search_fields: Allows admin to search users by these fields.
    - list_filter: Enables filtering users by streamer, staff, and active status.
    You can add more customizations as needed for better admin experience.
    """
    list_display = ('username', 'email', 'display_name', 'is_streamer', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'display_name')
    list_filter = ('is_streamer', 'is_staff', 'is_active')
    # Add more customizations as needed
