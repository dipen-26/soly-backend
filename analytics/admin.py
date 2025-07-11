"""
Admin configuration for the Analytics app of Soly - Live Streaming Platform.

This file registers all analytics-related models with the Django admin site and customizes their display for easier management.

Workflows:
- Each model is registered with a ModelAdmin class to control list display, search, and filtering in the admin UI.
- This helps platform admins review analytics, highlights, insights, ML models, and content analysis results efficiently.

Layman explanation:
- This file makes analytics data easy to view and manage in the Django admin dashboard, with search and filter options for each type of analytics record.
"""

from django.contrib import admin
from .models import StreamerAnalytics, ContentHighlight, StreamerInsights, MLModel, StreamContentAnalysis

@admin.register(StreamerAnalytics)
class StreamerAnalyticsAdmin(admin.ModelAdmin):
    # Show key fields for quick review in admin list view
    list_display = ('streamer', 'analyzed_at', 'overall_sentiment_score', 'engagement_score')
    search_fields = ('streamer__username',)

@admin.register(ContentHighlight)
class ContentHighlightAdmin(admin.ModelAdmin):
    list_display = ('stream', 'title', 'highlight_score', 'is_published')
    search_fields = ('stream__title', 'title')
    list_filter = ('is_published',)

@admin.register(StreamerInsights)
class StreamerInsightsAdmin(admin.ModelAdmin):
    list_display = ('streamer', 'generated_at')
    search_fields = ('streamer__username',)

@admin.register(MLModel)
class MLModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'model_type', 'is_active', 'trained_on')
    search_fields = ('name', 'model_type')
    list_filter = ('is_active',)

@admin.register(StreamContentAnalysis)
class StreamContentAnalysisAdmin(admin.ModelAdmin):
    list_display = ('stream', 'timestamp', 'inappropriate_content_score', 'violence_score')
    search_fields = ('stream__title',)
