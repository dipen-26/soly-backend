"""
content/models.py

This module defines the database models for the content system, including VODs (Video on Demand), highlights, playlists, tags, and metadata.
Models represent the structure of content data and provide fields for ML analysis, visibility, and user interaction.
"""

from django.db import models
from django.conf import settings

class VOD(models.Model):
    """
    Stores Video on Demand (VOD) entries, representing past broadcasts.
    Includes fields for metadata, visibility, ML-generated chapters/highlights/tags, and access control.
    """
    stream = models.OneToOneField('streams.Stream', on_delete=models.CASCADE)  # The stream this VOD is based on
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The streamer who owns the VOD
    title = models.CharField(max_length=200)  # Title of the VOD
    description = models.TextField(blank=True)  # Description of the VOD
    duration = models.DurationField()  # Duration of the VOD
    view_count = models.PositiveIntegerField(default=0)  # Number of views
    video_url = models.URLField()  # URL to the video file
    thumbnail = models.ImageField(upload_to='vod_thumbnails/')  # Thumbnail image for the VOD
    published_at = models.DateTimeField(auto_now_add=True)  # When the VOD was published
    
    # Visibility and Access
    is_public = models.BooleanField(default=True)  # True if VOD is public
    is_subscribers_only = models.BooleanField(default=False)  # True if only subscribers can view
    
    # ML/DL Generated Fields
    chapters = models.JSONField(default=list)  # Auto-generated stream chapters (list of timestamps)
    highlights = models.JSONField(default=list)  # Timestamps of interesting moments
    content_tags = models.JSONField(default=list)  # Auto-generated content tags
    category_predictions = models.JSONField(default=dict)  # ML predicted categories
    
    class Meta:
        ordering = ['-published_at']  # Newest VODs first
        indexes = [
            models.Index(fields=['streamer', 'published_at'])  # For fast lookup by streamer and date
        ]

class Highlight(models.Model):
    """
    Stores highlights from VODs, either auto-generated or manually created.
    Highlights are short, interesting segments of a stream or VOD.
    """
    vod = models.ForeignKey(VOD, on_delete=models.CASCADE)  # The VOD this highlight belongs to
    title = models.CharField(max_length=100)  # Title of the highlight
    description = models.TextField(blank=True)  # Description of the highlight
    start_time = models.DurationField()  # Start time in the VOD
    end_time = models.DurationField()  # End time in the VOD
    duration = models.DurationField()  # Duration of the highlight
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_highlights'
    )  # User who created the highlight
    view_count = models.PositiveIntegerField(default=0)  # Number of views
    like_count = models.PositiveIntegerField(default=0)  # Number of likes
    share_count = models.PositiveIntegerField(default=0)  # Number of shares
    
    # ML/DL Fields
    highlight_score = models.FloatField()  # ML-generated interestingness score
    auto_generated = models.BooleanField(default=False)  # True if highlight is auto-generated
    content_type = models.CharField(max_length=50)  # gameplay, reaction, discussion, etc.
    
    created_at = models.DateTimeField(auto_now_add=True)  # When the highlight was created
    
    class Meta:
        ordering = ['-highlight_score', '-created_at']  # Best highlights first

class Playlist(models.Model):
    """
    Model for organizing VODs and highlights into playlists
    """
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The user who created the playlist
    title = models.CharField(max_length=100)  # Title of the playlist
    description = models.TextField(blank=True)  # Description of the playlist
    thumbnail = models.ImageField(upload_to='playlist_thumbnails/', blank=True)  # Thumbnail for the playlist
    is_public = models.BooleanField(default=True)  # True if playlist is public
    created_at = models.DateTimeField(auto_now_add=True)  # When the playlist was created
    updated_at = models.DateTimeField(auto_now=True)  # When the playlist was last updated
    
    # ML/DL Fields
    auto_categorized = models.BooleanField(default=False)  # True if playlist is auto-categorized
    content_category = models.CharField(max_length=50, blank=True)  # Category of content in the playlist
    suggested_videos = models.JSONField(default=list)  # ML-suggested videos for playlist
    
    def __str__(self):
        return f"{self.title} by {self.creator.username}"  # Playlist title and creator

class PlaylistItem(models.Model):
    """
    Model for items within a playlist
    """
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)  # The playlist this item belongs to
    content_type = models.CharField(max_length=20)  # 'vod' or 'highlight'
    vod = models.ForeignKey(VOD, null=True, blank=True, on_delete=models.CASCADE)  # The VOD (if content_type is 'vod')
    highlight = models.ForeignKey(Highlight, null=True, blank=True, on_delete=models.CASCADE)  # The highlight (if content_type is 'highlight')
    order = models.PositiveIntegerField()  # Order of this item in the playlist
    added_at = models.DateTimeField(auto_now_add=True)  # When the item was added to the playlist
    
    class Meta:
        ordering = ['order']  # Order items by their sequence in the playlist
        unique_together = ('playlist', 'order')  # Ensure unique order for each playlist

class ContentTag(models.Model):
    """
    Model for content tagging and categorization
    """
    name = models.CharField(max_length=50, unique=True)  # Name of the tag
    category = models.CharField(max_length=50)  # game, topic, content_type, etc.
    created_at = models.DateTimeField(auto_now_add=True)  # When the tag was created
    usage_count = models.PositiveIntegerField(default=0)  # How many times the tag has been used
    
    # ML/DL Fields
    is_auto_generated = models.BooleanField(default=False)  # True if tag is auto-generated
    confidence_score = models.FloatField(null=True)  # ML confidence in auto-generated tags
    related_tags = models.JSONField(default=list)  # ML-discovered related tags
    
    def __str__(self):
        return self.name  # Tag name

class ContentMetadata(models.Model):
    """
    Model for storing additional content metadata and ML insights
    """
    vod = models.OneToOneField(VOD, null=True, blank=True, on_delete=models.CASCADE)  # The VOD this metadata belongs to
    highlight = models.OneToOneField(Highlight, null=True, blank=True, on_delete=models.CASCADE)  # The highlight this metadata belongs to
    
    # Content Analysis
    content_summary = models.TextField()  # AI-generated summary of the content
    key_moments = models.JSONField(default=list)  # Important timestamps with descriptions
    topics_discussed = models.JSONField(default=list)  # Main topics covered
    
    # Technical Metadata
    video_quality = models.CharField(max_length=20)  # Quality of the video (e.g., 720p, 1080p)
    frame_rate = models.PositiveIntegerField()  # Frame rate of the video
    audio_quality = models.CharField(max_length=20)  # Quality of the audio
    file_size = models.PositiveBigIntegerField()  # Size of the file in bytes
    
    # ML/DL Insights
    engagement_prediction = models.FloatField()  # Predicted engagement score
    recommended_thumbnail_time = models.DurationField(null=True)  # Recommended time for thumbnail
    auto_chapters = models.JSONField(default=list)  # AI-generated chapter markers
    scene_analysis = models.JSONField(default=dict)  # Detailed scene breakdown
    
    created_at = models.DateTimeField(auto_now_add=True)  # When the metadata was created
    updated_at = models.DateTimeField(auto_now=True)  # When the metadata was last updated
