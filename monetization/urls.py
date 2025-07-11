"""
monetization/urls.py

This module defines URL routes for the monetization app, mapping API endpoints to their corresponding viewsets.
Uses Django REST Framework's router to automatically generate RESTful routes for monetization features.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SubscriptionViewSet, ChannelPointsViewSet, PointsRewardViewSet, DonationViewSet,
    RevenueShareViewSet, TransactionViewSet, PayoutViewSet
)

# Router automatically generates RESTful routes for each monetization feature
router = DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'channel-points', ChannelPointsViewSet)
router.register(r'points-rewards', PointsRewardViewSet)
router.register(r'donations', DonationViewSet)
router.register(r'revenue-shares', RevenueShareViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'payouts', PayoutViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all monetization API endpoints
]

# This file connects HTTP requests to the correct view logic for monetization features.
