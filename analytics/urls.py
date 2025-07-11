"""
URL routing for the Analytics app of Soly - Live Streaming Platform.

This file defines all API endpoints for analytics, highlights, insights, ML models, and content analysis using DRF routers.

Workflows:
- Each ViewSet is registered with a router, which automatically creates RESTful endpoints for CRUD operations.
- All endpoints are included under the analytics app's base URL.

Layman explanation:
- This file connects the web URLs to the code that handles analytics data, so you can access analytics features via API calls.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StreamerAnalyticsViewSet, ContentHighlightViewSet, StreamerInsightsViewSet,
    MLModelViewSet, StreamContentAnalysisViewSet
)

router = DefaultRouter()
router.register(r'streamer-analytics', StreamerAnalyticsViewSet)
router.register(r'content-highlights', ContentHighlightViewSet)
router.register(r'streamer-insights', StreamerInsightsViewSet)
router.register(r'ml-models', MLModelViewSet)
router.register(r'stream-content-analysis', StreamContentAnalysisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
