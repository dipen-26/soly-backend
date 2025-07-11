"""
streams/admin.py

This module customizes the Django admin interface for streaming-related models.
It allows administrators to view, search, and filter streams, keys, qualities, metrics, and clips efficiently.
"""

from django.contrib import admin
from .models import Stream, StreamKey, StreamQuality, StreamMetrics, Clip

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for Stream objects.
    - list_display: Shows these fields in the stream list view.
    - search_fields: Allows admin to search streams by title and streamer.
    - list_filter: Enables filtering by live status and category.
    """
    list_display = ('streamer', 'title', 'is_live', 'started_at', 'ended_at')
    search_fields = ('title', 'streamer__username')
    list_filter = ('is_live', 'category')

@admin.register(StreamKey)
class StreamKeyAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for StreamKey objects.
    - list_display: Shows key details and usage status.
    - search_fields: Allows admin to search keys by streamer and key value.
    """
    list_display = ('streamer', 'key', 'is_active', 'last_used')
    search_fields = ('streamer__username', 'key')

@admin.register(StreamQuality)
class StreamQualityAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for StreamQuality objects.
    - list_display: Shows quality details and analytics.
    - search_fields: Allows admin to search qualities by stream and quality name.
    """
    list_display = ('stream', 'quality', 'bitrate', 'resolution', 'fps')
    search_fields = ('stream__title', 'quality')

@admin.register(StreamMetrics)
class StreamMetricsAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for StreamMetrics objects.
    - list_display: Shows metrics details and analytics.
    - search_fields: Allows admin to search metrics by stream title.
    - list_filter: Enables filtering by stream.
    """
    list_display = ('stream', 'timestamp', 'viewer_count', 'bitrate', 'fps')
    search_fields = ('stream__title',)
    list_filter = ('stream',)

@admin.register(Clip)
class ClipAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for Clip objects.
    - list_display: Shows clip details and highlight status.
    - search_fields: Allows admin to search clips by title and creator.
    - list_filter: Enables filtering by highlight status.
    """
    list_display = ('title', 'stream', 'creator', 'is_highlight', 'highlight_score')
    search_fields = ('title', 'creator__username')
    list_filter = ('is_highlight',)
