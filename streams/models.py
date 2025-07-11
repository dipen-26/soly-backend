"""
streams/models.py

This module defines the database models for the live streaming system, including streams and related features.
Models represent the structure of live stream data, supporting ML analysis, viewer engagement, and stream management.
"""

from django.db import models
from django.conf import settings
from django.utils import timezone

class Stream(models.Model):
    """
    Stores live streaming session details, including streamer, title, category, tags, and status.
    Includes fields for stream settings, viewer counts, ML sentiment/content safety, and highlight timestamps.
    """
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The user broadcasting the stream
    title = models.CharField(max_length=200)  # Title of the stream
    description = models.TextField(blank=True)  # Description of the stream
    category = models.CharField(max_length=50)  # Category (e.g., Gaming, Music)
    tags = models.JSONField(default=list)  # List of tags for search and categorization
    thumbnail = models.ImageField(upload_to='stream_thumbnails/', blank=True)  # Thumbnail image
    
    # Stream Status
    is_live = models.BooleanField(default=False)  # True if stream is currently live
    started_at = models.DateTimeField(null=True)  # When the stream started
    ended_at = models.DateTimeField(null=True)  # When the stream ended
    viewer_count = models.PositiveIntegerField(default=0)  # Current viewer count
    peak_viewers = models.PositiveIntegerField(default=0)  # Highest viewer count during stream
    
    # Stream Settings
    stream_quality = models.CharField(max_length=20, default='auto')  # Video quality setting
    is_mature_content = models.BooleanField(default=False)  # True if stream contains mature content
    chat_enabled = models.BooleanField(default=True)  # True if chat is enabled
    subscriber_only_chat = models.BooleanField(default=False)  # Only subscribers can chat
    followers_only_chat = models.BooleanField(default=False)  # Only followers can chat
    slow_mode = models.PositiveIntegerField(default=0)  # Seconds between messages, 0 for disabled
    
    # ML/DL Fields
    sentiment_score = models.FloatField(null=True)  # Overall chat sentiment (ML-generated)
    content_safety_score = models.FloatField(null=True)  # Content appropriateness score (ML-generated)
    highlight_timestamps = models.JSONField(default=list)  # Timestamps for auto-generated highlights
    
    created_at = models.DateTimeField(auto_now_add=True)  # When the stream record was created
    updated_at = models.DateTimeField(auto_now=True)  # When the stream record was last updated

    def __str__(self):
        # Returns a readable representation of the stream for admin and debugging
        return f"{self.streamer.username} - {self.title}"
    
    def start_stream(self):
        # Marks the stream as live and sets the start time
        self.is_live = True
        self.started_at = timezone.now()
        self.save()
    
    def end_stream(self):
        # Marks the stream as ended and sets the end time
        self.is_live = False
        self.ended_at = timezone.now()
        self.save()

class StreamKey(models.Model):
    """
    Model to manage stream keys for RTMP streaming
    """
    streamer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Stream Key for {self.streamer.username}"

class StreamQuality(models.Model):
    """
    Model to track different quality versions of the stream
    """
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    quality = models.CharField(max_length=20)  # 1080p, 720p, etc.
    bitrate = models.PositiveIntegerField()  # in kbps
    resolution = models.CharField(max_length=20)  # 1920x1080, 1280x720, etc.
    fps = models.PositiveIntegerField(default=30)

    class Meta:
        unique_together = ('stream', 'quality')

class StreamMetrics(models.Model):
    """
    Model to store real-time stream metrics
    """
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    viewer_count = models.PositiveIntegerField()
    chat_message_count = models.PositiveIntegerField()
    bitrate = models.PositiveIntegerField()  # Current bitrate in kbps
    fps = models.FloatField()  # Current FPS
    cpu_usage = models.FloatField()  # CPU usage percentage
    memory_usage = models.FloatField()  # Memory usage in MB
    dropped_frames = models.PositiveIntegerField()
    
    class Meta:
        indexes = [
            models.Index(fields=['stream', 'timestamp'])
        ]

class Clip(models.Model):
    """
    Model for stream clips (short segments of streams)
    """
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()  # When in the stream the clip starts
    duration = models.PositiveIntegerField()  # Duration in seconds
    view_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to='clip_thumbnails/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ML/DL Fields
    is_highlight = models.BooleanField(default=False)  # Auto-detected highlight
    highlight_score = models.FloatField(null=True)  # Score indicating how interesting the moment is
    
    def __str__(self):
        return f"{self.title} - by {self.creator.username}"
