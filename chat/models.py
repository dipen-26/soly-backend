"""
chat/models.py

This module defines the database models for the chat system, including chat messages and custom emotes.
Models represent the structure of chat data and provide fields for moderation, ML analysis, and user interaction.
"""

from django.db import models
from django.conf import settings
from django.utils import timezone

class ChatMessage(models.Model):
    """
    Stores individual chat messages sent by users during a live stream.
    Includes fields for moderation, message type, and ML analysis (sentiment, toxicity, language).
    """
    stream = models.ForeignKey('streams.Stream', on_delete=models.CASCADE)  # The stream this message belongs to
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The user who sent the message
    message = models.TextField()  # The actual chat message text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the message was sent
    
    # Message Type and Status
    message_type = models.CharField(max_length=20, default='text')  # e.g., text, emote, announcement
    is_moderated = models.BooleanField(default=False)  # True if message was reviewed by a moderator
    is_deleted = models.BooleanField(default=False)  # True if message was deleted
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='deleted_messages'
    )  # The moderator who deleted the message, if any
    
    # ML/DL Fields
    sentiment_score = models.FloatField(null=True)  # Score from sentiment analysis (-1 to 1)
    toxicity_score = models.FloatField(null=True)  # Score from toxicity detection (0 to 1)
    language_detected = models.CharField(max_length=10, null=True)  # Detected language code (e.g., 'en')
    
    class Meta:
        indexes = [
            models.Index(fields=['stream', 'created_at']),  # For fast lookup of messages in a stream
            models.Index(fields=['user', 'created_at'])      # For fast lookup of messages by user
        ]

class ChatEmote(models.Model):
    """
    Stores custom emotes that streamers can use in their chat.
    Emotes can be static or animated, and may require a subscription tier to use.
    """
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The streamer who owns the emote
    name = models.CharField(max_length=50)  # Name of the emote (e.g., 'hype')
    image = models.ImageField(upload_to='emotes/')  # Image file for the emote
    is_animated = models.BooleanField(default=False)  # True if emote is animated
    tier_required = models.PositiveIntegerField(default=0)  # Subscription tier required to use (0 = all users)
    is_active = models.BooleanField(default=True)  # True if emote is available for use
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when emote was created

    class Meta:
        unique_together = ('streamer', 'name')  # Each streamer can only have one emote with a given name

class ChatCommand(models.Model):
    """
    Model to store custom chat commands
    """
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    command = models.CharField(max_length=50)
    response = models.TextField()
    cooldown = models.PositiveIntegerField(default=0)  # Cooldown in seconds
    user_level = models.CharField(max_length=20, default='all')  # all, subscriber, mod, vip
    is_active = models.BooleanField(default=True)
    usage_count = models.PositiveIntegerField(default=0)
    last_used = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('streamer', 'command')

class ChatModerationRule(models.Model):
    """
    Model to store chat moderation rules
    """
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rule_type = models.CharField(max_length=20)  # banned_words, link_filter, caps_filter, etc.
    rule_data = models.JSONField()  # Flexible structure for different rule types
    action = models.CharField(max_length=20)  # delete, timeout, ban
    action_duration = models.PositiveIntegerField(default=0)  # Duration in seconds for timeout
    is_active = models.BooleanField(default=True)
    
    # ML/DL Enhancement
    ml_assisted = models.BooleanField(default=False)  # Whether ML helps in detection
    sensitivity = models.FloatField(default=0.5)  # Threshold for ML detection
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ChatBot(models.Model):
    """
    Model to store chatbot configurations and actions
    """
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    # Bot Capabilities
    can_moderate = models.BooleanField(default=False)
    can_respond = models.BooleanField(default=True)
    can_schedule_messages = models.BooleanField(default=True)
    
    # AI/ML Features
    uses_ml = models.BooleanField(default=False)
    personality_type = models.CharField(max_length=50, default='friendly')
    learning_enabled = models.BooleanField(default=False)
    
    # Customization
    custom_responses = models.JSONField(default=dict)
    scheduled_messages = models.JSONField(default=list)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('streamer', 'name')
