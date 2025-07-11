"""
notifications/admin.py

This module customizes the Django admin interface for notification-related models.
It allows administrators to view, search, and filter notifications, preferences, schedules, metrics, and smart rules efficiently.
"""

from django.contrib import admin
from .models import Notification, NotificationPreference, NotificationSchedule, NotificationMetrics, SmartNotificationRule

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for Notification objects.
    - list_display: Shows these fields in the notification list view.
    - search_fields: Allows admin to search notifications by user, title, and type.
    - list_filter: Enables filtering by read status and notification type.
    """
    list_display = ('user', 'title', 'notification_type', 'is_read', 'created_at', 'priority_score')
    search_fields = ('user__username', 'title', 'notification_type')
    list_filter = ('is_read', 'notification_type')

@admin.register(NotificationPreference)
class NotificationPreferenceAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for NotificationPreference objects.
    - list_display: Shows preference details and smart notification status.
    - search_fields: Allows admin to search preferences by user.
    - list_filter: Enables filtering by smart notification status.
    """
    list_display = ('user', 'smart_notifications', 'priority_threshold')
    search_fields = ('user__username',)
    list_filter = ('smart_notifications',)

@admin.register(NotificationSchedule)
class NotificationScheduleAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for NotificationSchedule objects.
    - list_display: Shows schedule details and status.
    - search_fields: Allows admin to search schedules by title and creator.
    - list_filter: Enables filtering by active status and schedule type.
    """
    list_display = ('title', 'schedule_type', 'scheduled_time', 'is_active', 'created_by')
    search_fields = ('title', 'created_by__username')
    list_filter = ('is_active', 'schedule_type')

@admin.register(NotificationMetrics)
class NotificationMetricsAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for NotificationMetrics objects.
    - list_display: Shows metrics details and engagement scores.
    - list_filter: Enables filtering by click status.
    """
    list_display = ('notification', 'delivered_at', 'read_at', 'clicked', 'clicked_at', 'engagement_score')
    list_filter = ('clicked',)

@admin.register(SmartNotificationRule)
class SmartNotificationRuleAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for SmartNotificationRule objects.
    - list_display: Shows rule details, ML model, and performance stats.
    - search_fields: Allows admin to search rules by name and ML model.
    - list_filter: Enables filtering by active status.
    """
    list_display = ('name', 'is_active', 'ml_model', 'success_rate', 'total_processed', 'last_updated')
    search_fields = ('name', 'ml_model')
    list_filter = ('is_active',)
