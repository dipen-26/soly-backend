"""
streams/urls.py

This module defines URL routes for the streams app, mapping API endpoints to their corresponding viewsets.
Uses Django REST Framework's router to automatically generate RESTful routes for streaming features.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StreamViewSet, StreamKeyViewSet, StreamQualityViewSet, StreamMetricsViewSet, ClipViewSet

# Router automatically generates RESTful routes for each streaming feature
router = DefaultRouter()
router.register(r'streams', StreamViewSet)
router.register(r'stream-keys', StreamKeyViewSet)
router.register(r'stream-qualities', StreamQualityViewSet)
router.register(r'stream-metrics', StreamMetricsViewSet)
router.register(r'clips', ClipViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all streaming API endpoints
]

# This file connects HTTP requests to the correct view logic for streaming features.
