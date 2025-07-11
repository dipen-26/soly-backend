"""
content/serializers.py

This module defines serializers for content-related models, converting model instances to JSON for API responses
and validating incoming data for VODs, highlights, playlists, tags, and metadata.
"""

from rest_framework import serializers
from .models import VOD, Highlight, Playlist, PlaylistItem, ContentTag, ContentMetadata

class VODSerializer(serializers.ModelSerializer):
    """
    Serializes VOD objects for API input/output.
    All fields are included for full VOD details.
    """
    class Meta:
        model = VOD
        fields = '__all__'  # Includes all fields from the VOD model

class HighlightSerializer(serializers.ModelSerializer):
    """
    Serializes Highlight objects for API input/output.
    Used for uploading, listing, and managing highlights.
    """
    class Meta:
        model = Highlight
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    """
    Serializes Playlist objects for API input/output.
    Used for managing playlists of VODs and highlights.
    """
    class Meta:
        model = Playlist
        fields = '__all__'

class PlaylistItemSerializer(serializers.ModelSerializer):
    """
    Serializes PlaylistItem objects for API input/output.
    Used for managing items within playlists.
    """
    class Meta:
        model = PlaylistItem
        fields = '__all__'

class ContentTagSerializer(serializers.ModelSerializer):
    """
    Serializes ContentTag objects for API input/output.
    Used for managing tags associated with content for search and categorization.
    """
    class Meta:
        model = ContentTag
        fields = '__all__'

class ContentMetadataSerializer(serializers.ModelSerializer):
    """
    Serializes ContentMetadata objects for API input/output.
    Used for managing technical metadata about content (quality, file size, etc.).
    """
    class Meta:
        model = ContentMetadata
        fields = '__all__'
