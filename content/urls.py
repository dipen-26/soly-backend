"""
content/urls.py

This module defines URL routes for the content app, mapping API endpoints to their corresponding viewsets.
Uses Django REST Framework's router to automatically generate RESTful routes for content features.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VODViewSet, HighlightViewSet, PlaylistViewSet, PlaylistItemViewSet, ContentTagViewSet, ContentMetadataViewSet

# Router automatically generates RESTful routes for each content feature
router = DefaultRouter()
router.register(r'vods', VODViewSet)
router.register(r'highlights', HighlightViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'playlist-items', PlaylistItemViewSet)
router.register(r'content-tags', ContentTagViewSet)
router.register(r'content-metadata', ContentMetadataViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all content API endpoints
]

# This file connects HTTP requests to the correct view logic for content features.
