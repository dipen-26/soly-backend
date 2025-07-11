"""
Models for the Analytics app of Soly - Live Streaming Platform.

This module defines all database models related to analytics, highlights, insights, ML model management, and real-time content analysis.

Each model is designed to support advanced ML/DL workflows, streamer performance tracking, and platform intelligence features.

Workflows:
- StreamerAnalytics: Stores ML-generated metrics for streamers, such as sentiment, engagement, and growth.
- ContentHighlight: Stores highlights detected by ML or created manually, with metadata for publishing and discovery.
- StreamerInsights: Stores actionable recommendations and insights for streamers, generated by AI.
- MLModel: Tracks ML model versions, performance, and metadata for platform intelligence.
- StreamContentAnalysis: Stores real-time analysis results for live streams, including safety and engagement metrics.

All models use Django ORM and support JSON fields for flexible ML/DL data storage.
"""

from django.db import models
from django.conf import settings
import numpy as np

class StreamerAnalytics(models.Model):
    """
    Stores ML/DL based analytics for streamers.
    - Each record is linked to a streamer (user).
    - Sentiment, engagement, and growth metrics are stored for platform intelligence.
    """
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    analyzed_at = models.DateTimeField(auto_now=True)
    # Overall sentiment score for the streamer (range: -1 to 1)
    overall_sentiment_score = models.FloatField(default=0.0)
    # Detailed sentiment breakdown (e.g., positive, negative, neutral)
    sentiment_breakdown = models.JSONField(default=dict)
    # ML-predicted content categories for the streamer
    content_category_predictions = models.JSONField(default=dict)
    # Auto-generated content tags for discoverability
    content_tags = models.JSONField(default=list)
    # Engagement score and factors (e.g., chat activity, viewer retention)
    engagement_score = models.FloatField(default=0.0)
    engagement_factors = models.JSONField(default=dict)
    # Predicted growth rate and factors
    growth_rate = models.FloatField(null=True)
    growth_factors = models.JSONField(default=dict)
    
    class Meta:
        verbose_name_plural = 'Streamer Analytics'

class ContentHighlight(models.Model):
    """
    Stores automatically generated or manually created stream highlights.
    - Each highlight is linked to a stream.
    - ML-generated scores and metadata help with highlight discovery and publishing.
    """
    stream = models.ForeignKey('streams.Stream', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    highlight_score = models.FloatField()  # ML-generated interestingness score
    # Chat intensity and viewer spike help ML score highlights
    chat_intensity = models.FloatField()
    viewer_spike = models.FloatField()
    event_type = models.CharField(max_length=50)
    # AI-generated title, description, tags, and thumbnail timestamp
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.JSONField(default=list)
    thumbnail_timestamp = models.FloatField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Returns a readable string for admin and debugging
        return f"{self.stream.title} - {self.title}"

class StreamerInsights(models.Model):
    """
    Stores AI-generated insights and recommendations for streamers.
    - Used to help streamers optimize their content and growth.
    - Includes best times to stream, content recommendations, audience insights, and competitor analysis.
    """
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)
    # AI-recommended streaming times and durations
    best_streaming_times = models.JSONField(default=list)
    optimal_stream_duration = models.JSONField(default=dict)
    content_recommendations = models.JSONField(default=list)
    # Audience demographics, interests, and engagement patterns
    audience_demographics = models.JSONField(default=dict)
    audience_interests = models.JSONField(default=list)
    audience_engagement_patterns = models.JSONField(default=dict)
    # Growth opportunities, improvement areas, and competitor analysis
    growth_opportunities = models.JSONField(default=list)
    improvement_areas = models.JSONField(default=list)
    competitor_analysis = models.JSONField(default=dict)

    def __str__(self):
        # Returns a readable string for admin and debugging
        return f"Insights for {self.streamer.username}"

class MLModel(models.Model):
    """
    Manages ML model versions and metadata for platform intelligence.
    - Tracks model performance, training data, and active status.
    - Used for sentiment analysis, highlight detection, and more.
    """
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    model_type = models.CharField(max_length=50)
    model_file = models.FileField(upload_to='ml_models/')
    is_active = models.BooleanField(default=True)
    # Model performance metrics
    accuracy = models.FloatField(null=True)
    precision = models.FloatField(null=True)
    recall = models.FloatField(null=True)
    f1_score = models.FloatField(null=True)
    # Training information
    trained_on = models.DateTimeField()
    training_data_size = models.PositiveIntegerField()
    last_evaluation = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Returns a readable string for admin and debugging
        return f"{self.name} v{self.version}"

class StreamContentAnalysis(models.Model):
    """
    Stores real-time content analysis results for live streams.
    - Used for content safety, engagement, and ML-driven moderation.
    - Includes audio, visual, and safety metrics.
    """
    stream = models.ForeignKey('streams.Stream', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Content safety analysis (ML-generated scores)
    inappropriate_content_score = models.FloatField()
    violence_score = models.FloatField()
    adult_content_score = models.FloatField()
    hate_speech_score = models.FloatField()
    # Audio analysis
    noise_level = models.FloatField()
    speech_clarity = models.FloatField()
    music_detected = models.BooleanField()
    # Visual analysis
    brightness_score = models.FloatField()
    motion_score = models.FloatField()
    scene_changes = models.PositiveIntegerField()
    object_detection_results = models.JSONField(default=list)

    class Meta:
        indexes = [
            models.Index(fields=['stream', 'timestamp'])
        ]
