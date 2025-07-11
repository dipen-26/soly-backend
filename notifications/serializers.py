"""
notifications/serializers.py

This module defines serializers for notification-related models, converting model instances to JSON for API responses
and validating incoming data for notifications, preferences, schedules, metrics, and smart rules.
"""

from rest_framework import serializers
from .models import Notification, NotificationPreference, NotificationSchedule, NotificationMetrics, SmartNotificationRule

class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializes Notification objects for API input/output.
    All fields are included for full notification details.
    """
    class Meta:
        model = Notification
        fields = '__all__'  # Includes all fields from the Notification model

class NotificationPreferenceSerializer(serializers.ModelSerializer):
    """
    Serializes NotificationPreference objects for API input/output.
    Used for managing user notification preferences.
    """
    class Meta:
        model = NotificationPreference
        fields = '__all__'

class NotificationScheduleSerializer(serializers.ModelSerializer):
    """
    Serializes NotificationSchedule objects for API input/output.
    Used for managing scheduled notifications (e.g., reminders).
    """
    class Meta:
        model = NotificationSchedule
        fields = '__all__'

class NotificationMetricsSerializer(serializers.ModelSerializer):
    """
    Serializes NotificationMetrics objects for API input/output.
    Used for managing analytics and engagement metrics for notifications.
    """
    class Meta:
        model = NotificationMetrics
        fields = '__all__'

class SmartNotificationRuleSerializer(serializers.ModelSerializer):
    """
    Serializes SmartNotificationRule objects for API input/output.
    Used for managing ML-driven notification rules and targeting.
    """
    class Meta:
        model = SmartNotificationRule
        fields = '__all__'
