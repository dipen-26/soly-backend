"""
content/admin.py

This module customizes the Django admin interface for content-related models.
It allows administrators to view, search, and filter VODs, highlights, playlists, tags, and metadata efficiently.
"""

from django.contrib import admin
from .models import VOD, Highlight, Playlist, PlaylistItem, ContentTag, ContentMetadata

@admin.register(VOD)
class VODAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for VOD objects.
    - list_display: Shows these fields in the VOD list view.
    - search_fields: Allows admin to search VODs by title and streamer.
    - list_filter: Enables filtering by public and subscriber-only status.
    """
    list_display = ('title', 'streamer', 'duration', 'view_count', 'published_at', 'is_public')
    search_fields = ('title', 'streamer__username')
    list_filter = ('is_public', 'is_subscribers_only')

@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for Highlight objects.
    - list_display: Shows highlight details and ML score.
    - search_fields: Allows admin to search highlights by title and creator.
    - list_filter: Enables filtering by auto-generated status and content type.
    """
    list_display = ('title', 'vod', 'created_by', 'highlight_score', 'auto_generated', 'created_at')
    search_fields = ('title', 'created_by__username')
    list_filter = ('auto_generated', 'content_type')

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for Playlist objects.
    - list_display: Shows playlist details.
    - search_fields: Allows admin to search playlists by title and creator.
    - list_filter: Enables filtering by public status.
    """
    list_display = ('title', 'creator', 'is_public', 'created_at')
    search_fields = ('title', 'creator__username')
    list_filter = ('is_public',)

@admin.register(PlaylistItem)
class PlaylistItemAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for PlaylistItem objects.
    - list_display: Shows item details and order.
    - list_filter: Enables filtering by content type.
    """
    list_display = ('playlist', 'content_type', 'order', 'added_at')
    list_filter = ('content_type',)

@admin.register(ContentTag)
class ContentTagAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for ContentTag objects.
    - list_display: Shows tag details and usage stats.
    - search_fields: Allows admin to search tags by name and category.
    - list_filter: Enables filtering by auto-generated status and category.
    """
    list_display = ('name', 'category', 'usage_count', 'is_auto_generated')
    search_fields = ('name', 'category')
    list_filter = ('is_auto_generated', 'category')

@admin.register(ContentMetadata)
class ContentMetadataAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for ContentMetadata objects.
    - list_display: Shows metadata details (quality, file size, etc.).
    - list_filter: Enables filtering by video and audio quality.
    """
    list_display = ('vod', 'highlight', 'video_quality', 'frame_rate', 'audio_quality', 'file_size')
    list_filter = ('video_quality', 'audio_quality')
