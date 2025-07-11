"""
streams/serializers.py

This module defines serializers for streaming-related models, converting model instances to JSON for API responses
and validating incoming data for streams, keys, qualities, metrics, and clips.
"""

from rest_framework import serializers
from .models import Stream, StreamKey, StreamQuality, StreamMetrics, Clip

class StreamSerializer(serializers.ModelSerializer):
    """
    Serializes Stream objects for API input/output.
    All fields are included for full stream details.
    """
    class Meta:
        model = Stream
        fields = '__all__'  # Includes all fields from the Stream model

class StreamKeySerializer(serializers.ModelSerializer):
    """
    Serializes StreamKey objects for API input/output.
    Used for managing stream keys for authentication and security.
    """
    class Meta:
        model = StreamKey
        fields = '__all__'

class StreamQualitySerializer(serializers.ModelSerializer):
    """
    Serializes StreamQuality objects for API input/output.
    Used for managing video quality settings and analytics.
    """
    class Meta:
        model = StreamQuality
        fields = '__all__'

class StreamMetricsSerializer(serializers.ModelSerializer):
    """
    Serializes StreamMetrics objects for API input/output.
    Used for managing real-time metrics and analytics for streams.
    """
    class Meta:
        model = StreamMetrics
        fields = '__all__'

class ClipSerializer(serializers.ModelSerializer):
    """
    Serializes Clip objects for API input/output.
    Used for managing stream clips and highlights.
    """
    class Meta:
        model = Clip
        fields = '__all__'
