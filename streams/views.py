"""
streams/views.py

This module defines API views for streaming features, including streams, keys, qualities, metrics, and clips.
Views handle HTTP requests, interact with models and serializers, and implement custom logic for ML highlight detection, analytics, and stream management.
"""

from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Stream, StreamKey, StreamQuality, StreamMetrics, Clip
from .serializers import StreamSerializer, StreamKeySerializer, StreamQualitySerializer, StreamMetricsSerializer, ClipSerializer

# StreamViewSet handles CRUD operations for streams
class StreamViewSet(viewsets.ModelViewSet):
    """
    Provides API endpoints for creating, reading, updating, and deleting streams.
    Only authenticated users can interact with streams.
    Custom logic for starting/stopping streams, live status, or ML highlight triggers can be added here.
    """
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
    permission_classes = [permissions.IsAuthenticated]
    # ML/DL stub: Call highlight generation and content safety models on live streams

# StreamKeyViewSet handles CRUD operations for stream keys
class StreamKeyViewSet(viewsets.ModelViewSet):
    """
    Provides API endpoints for managing stream keys for authentication and security.
    Only authenticated users can interact with stream keys.
    Custom logic for stream key generation, validation, or rotation can be added here.
    """
    queryset = StreamKey.objects.all()
    serializer_class = StreamKeySerializer
    permission_classes = [permissions.IsAuthenticated]

# StreamQualityViewSet handles CRUD operations for stream qualities
class StreamQualityViewSet(viewsets.ModelViewSet):
    """
    Provides API endpoints for managing video quality settings and analytics.
    Only authenticated users can interact with stream qualities.
    Custom logic for quality switching, analytics, or recommendations can be added here.
    """
    queryset = StreamQuality.objects.all()
    serializer_class = StreamQualitySerializer
    permission_classes = [permissions.IsAuthenticated]

# StreamMetricsViewSet handles CRUD operations for stream metrics
class StreamMetricsViewSet(viewsets.ModelViewSet):
    """
    Provides API endpoints for managing real-time metrics and analytics for streams.
    Only authenticated users can interact with stream metrics.
    Custom logic for real-time metrics, ML anomaly detection, or reporting can be added here.
    """
    queryset = StreamMetrics.objects.all()
    serializer_class = StreamMetricsSerializer
    permission_classes = [permissions.IsAuthenticated]
    # ML/DL stub: Use ML to detect anomalies in stream metrics

# ClipViewSet handles CRUD operations for stream clips
class ClipViewSet(viewsets.ModelViewSet):
    """
    Provides API endpoints for managing stream clips and highlights.
    Only authenticated users can interact with clips.
    Custom logic for clip creation, highlight detection, or sharing can be added here.
    """
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer
    permission_classes = [permissions.IsAuthenticated]
    # ML/DL stub: Use ML to auto-detect and score highlights
