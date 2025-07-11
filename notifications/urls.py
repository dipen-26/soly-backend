"""
notifications/urls.py

This module defines URL routes for the notifications app, mapping API endpoints to their corresponding viewsets.
Uses Django REST Framework's router to automatically generate RESTful routes for notification features.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NotificationViewSet, NotificationPreferenceViewSet, NotificationScheduleViewSet,
    NotificationMetricsViewSet, SmartNotificationRuleViewSet
)

# Router automatically generates RESTful routes for each notification feature
router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)
router.register(r'preferences', NotificationPreferenceViewSet)
router.register(r'schedules', NotificationScheduleViewSet)
router.register(r'metrics', NotificationMetricsViewSet)
router.register(r'smart-rules', SmartNotificationRuleViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all notification API endpoints
]

# This file connects HTTP requests to the correct view logic for notification features.
