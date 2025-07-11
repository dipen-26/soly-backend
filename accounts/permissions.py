"""
accounts/permissions.py

This module defines custom permission classes for the accounts app.
Permissions control which users can access specific API endpoints based on their roles (streamer, admin, viewer).
"""

from rest_framework import permissions

class IsStreamer(permissions.BasePermission):
    """
    Allows access only to streamer users.
    Streamers are users who can broadcast live streams on the platform.
    """
    def has_permission(self, request, view):
        # Checks if the user is authenticated and has the 'is_streamer' attribute set to True
        return bool(request.user and request.user.is_authenticated and getattr(request.user, 'is_streamer', False))

class IsAdmin(permissions.BasePermission):
    """
    Allows access only to admin users.
    Admins have elevated privileges to manage the platform and other users.
    """
    def has_permission(self, request, view):
        # Checks if the user is authenticated and is marked as staff (admin)
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)

class IsViewer(permissions.BasePermission):
    """
    Allows access only to non-streamer, non-admin users (viewers).
    Viewers are regular users who watch streams but do not broadcast or manage the platform.
    """
    def has_permission(self, request, view):
        # Checks if the user is authenticated and is neither staff nor streamer
        return bool(request.user and request.user.is_authenticated and not request.user.is_staff and not getattr(request.user, 'is_streamer', False))
