"""
notifications/models.py

This module defines the database models for the notifications system, including user notifications and notification preferences.
Models represent the structure of notification data, supporting ML prioritization, user targeting, and engagement prediction.
"""

from django.db import models
from django.conf import settings

class Notification(models.Model):
    """
    Stores notifications sent to users, such as stream starts, new followers, donations, etc.
    Includes fields for notification type, read status, ML priority score, and engagement prediction.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The user receiving the notification
    title = models.CharField(max_length=100)  # Title of the notification
    message = models.TextField()  # Notification message content
    notification_type = models.CharField(max_length=50)  # Type of notification (e.g., stream_start, follower)
    is_read = models.BooleanField(default=False)  # True if user has read the notification
    created_at = models.DateTimeField(auto_now_add=True)  # When the notification was created
    
    # Optional related models
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='sent_notifications'
    )  # The user who triggered the notification (e.g., follower, donor)
    related_stream = models.ForeignKey(
        'streams.Stream',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )  # The stream related to the notification, if any
    
    # ML/DL Fields
    priority_score = models.FloatField(default=0.0)  # ML-determined importance of the notification
    user_engagement_prediction = models.FloatField(null=True)  # Predicted user engagement with this notification
    
    class Meta:
        ordering = ['-created_at']  # Newest notifications first
        indexes = [
            models.Index(fields=['user', 'created_at']),  # For fast lookup by user and date
            models.Index(fields=['user', 'is_read'])      # For fast lookup by user and read status
        ]

class NotificationPreference(models.Model):
    """
    Stores user preferences for receiving different types of notifications.
    Allows users to customize which notifications they want to receive.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The user whose preferences are stored
    
    # Stream Notifications
    live_streams = models.BooleanField(default=True)  # Receive notifications for live streams
    stream_reminders = models.BooleanField(default=True)  # Receive reminders for upcoming streams
    vod_uploads = models.BooleanField(default=True)  # Receive notifications for VOD uploads
    
    # Social Notifications
    new_followers = models.BooleanField(default=True)  # Receive notifications for new followers
    mentions = models.BooleanField(default=True)  # Receive notifications when mentioned
    chat_highlights = models.BooleanField(default=True)  # Receive highlights from chat
    
    # Engagement Notifications
    donations = models.BooleanField(default=True)  # Receive notifications for donations
    subscriptions = models.BooleanField(default=True)  # Receive notifications for new subscriptions
    achievements = models.BooleanField(default=True)  # Receive notifications for achievements
    
    # Channel Updates
    streamer_announcements = models.BooleanField(default=True)  # Receive announcements from the streamer
    schedule_changes = models.BooleanField(default=True)  # Receive notifications for schedule changes
    
    # Delivery Preferences
    email_notifications = models.BooleanField(default=True)  # Receive notifications via email
    push_notifications = models.BooleanField(default=True)  # Receive push notifications on mobile
    notification_schedule = models.JSONField(default=dict)  # Custom scheduling preferences
    
    # ML/DL Enhanced Features
    smart_notifications = models.BooleanField(default=True)  # Use ML for notification filtering
    priority_threshold = models.FloatField(default=0.5)  # Minimum priority score for notifications
    
    def __str__(self):
        return f"Notification Preferences for {self.user.username}"

class NotificationSchedule(models.Model):
    """
    Model for scheduled notifications
    """
    title = models.CharField(max_length=100)  # Title of the scheduled notification
    message = models.TextField()  # Message content of the notification
    schedule_type = models.CharField(max_length=20)  # Type of schedule (one_time, recurring, smart)
    scheduled_time = models.DateTimeField()  # When the notification is scheduled to be sent
    target_users = models.ManyToManyField(settings.AUTH_USER_MODEL)  # Users targeted by this notification
    is_active = models.BooleanField(default=True)  # True if the schedule is active
    
    # For recurring notifications
    recurrence_pattern = models.JSONField(null=True, blank=True)  # Pattern for recurring notifications
    last_sent = models.DateTimeField(null=True)  # When the notification was last sent
    
    # ML/DL Features
    smart_targeting = models.BooleanField(default=False)  # Use ML for user targeting
    engagement_optimization = models.BooleanField(default=False)  # Optimize timing for engagement
    
    created_at = models.DateTimeField(auto_now_add=True)  # When the schedule was created
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_schedules'
    )  # The user who created the schedule
    
    def __str__(self):
        return self.title

class NotificationMetrics(models.Model):
    """
    Model for tracking notification performance and analytics
    """
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)  # The notification being tracked
    delivered_at = models.DateTimeField()  # When the notification was delivered
    read_at = models.DateTimeField(null=True)  # When the notification was read
    clicked = models.BooleanField(default=False)  # True if the notification was clicked
    clicked_at = models.DateTimeField(null=True)  # When the notification was clicked
    
    # Engagement Metrics
    time_to_read = models.DurationField(null=True)  # Time between delivery and read
    time_to_click = models.DurationField(null=True)  # Time between delivery and click
    user_action_taken = models.BooleanField(default=False)  # True if the user took an action
    
    # Device Info
    device_type = models.CharField(max_length=50, null=True)  # Type of device used
    platform = models.CharField(max_length=50, null=True)  # Platform (e.g., iOS, Android, Web)
    
    # ML/DL Analytics
    engagement_score = models.FloatField(null=True)  # ML-calculated engagement score
    effectiveness_score = models.FloatField(null=True)  # Overall effectiveness rating
    
    class Meta:
        indexes = [
            models.Index(fields=['notification', 'delivered_at'])  # For fast lookup by notification and delivery date
        ]

class SmartNotificationRule(models.Model):
    """
    Model for ML-driven notification rules and filtering
    """
    name = models.CharField(max_length=100)  # Name of the smart notification rule
    description = models.TextField()  # Description of what the rule does
    is_active = models.BooleanField(default=True)  # True if the rule is active
    
    # Rule Configuration
    notification_types = models.JSONField()  # Types of notifications this rule applies to
    user_segments = models.JSONField(default=list)  # Target user segments
    
    # ML/DL Parameters
    ml_model = models.CharField(max_length=50)  # Reference to the ML model to use
    minimum_relevance_score = models.FloatField(default=0.5)  # Minimum score for relevance
    engagement_threshold = models.FloatField(default=0.3)  # Minimum engagement score to trigger action
    
    # Rule Logic
    conditions = models.JSONField()  # Complex conditions for notification filtering
    actions = models.JSONField()  # Actions to take based on conditions
    
    # Performance Tracking
    success_rate = models.FloatField(default=0.0)  # Success rate of the rule
    total_processed = models.PositiveIntegerField(default=0)  # Total notifications processed by this rule
    last_updated = models.DateTimeField(auto_now=True)  # When the rule was last updated
    
    def __str__(self):
        return self.name
