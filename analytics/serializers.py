"""
Serializers for the Analytics app of Soly - Live Streaming Platform.

These serializers convert model instances to JSON for API responses and validate incoming data for analytics-related endpoints.

Workflows:
- Each serializer is mapped to a model and exposes all fields for flexible ML/DL data exchange.
- Used by DRF ViewSets to handle API requests and responses for analytics, highlights, insights, ML models, and content analysis.
"""

from rest_framework import serializers
from .models import StreamerAnalytics, ContentHighlight, StreamerInsights, MLModel, StreamContentAnalysis

class StreamerAnalyticsSerializer(serializers.ModelSerializer):
    """
    Serializer for StreamerAnalytics model.
    Converts streamer analytics records to JSON and validates incoming data.
    """

    class Meta:
        model = StreamerAnalytics
        fields = '__all__'

class ContentHighlightSerializer(serializers.ModelSerializer):
    """
    Serializer for ContentHighlight model.
    Handles highlight data for API endpoints.
    """

    class Meta:
        model = ContentHighlight
        fields = '__all__'

class StreamerInsightsSerializer(serializers.ModelSerializer):
    """
    Serializer for StreamerInsights model.
    Used for insights and recommendations API endpoints.
    """

    class Meta:
        model = StreamerInsights
        fields = '__all__'

class MLModelSerializer(serializers.ModelSerializer):
    """
    Serializer for MLModel model.
    Used for ML model management endpoints.
    """

    class Meta:
        model = MLModel
        fields = '__all__'

class StreamContentAnalysisSerializer(serializers.ModelSerializer):
    """
    Serializer for StreamContentAnalysis model.
    Used for real-time content analysis API endpoints.
    """

    class Meta:
        model = StreamContentAnalysis
        fields = '__all__'
