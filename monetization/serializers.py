"""
monetization/serializers.py

This module defines serializers for monetization-related models, converting model instances to JSON for API responses
and validating incoming data for subscriptions, points, rewards, donations, revenue sharing, transactions, and payouts.
"""

from rest_framework import serializers
from .models import Subscription, ChannelPoints, PointsReward, Donation, RevenueShare, Transaction, Payout

class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Serializes Subscription objects for API input/output.
    All fields are included for full subscription details.
    """
    class Meta:
        model = Subscription
        fields = '__all__'  # Includes all fields from the Subscription model

class ChannelPointsSerializer(serializers.ModelSerializer):
    """
    Serializes ChannelPoints objects for API input/output.
    Used for managing user points and balances.
    """
    class Meta:
        model = ChannelPoints
        fields = '__all__'

class PointsRewardSerializer(serializers.ModelSerializer):
    """
    Serializes PointsReward objects for API input/output.
    Used for managing rewards that can be redeemed with points.
    """
    class Meta:
        model = PointsReward
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    """
    Serializes Donation objects for API input/output.
    Used for managing user donations to streamers.
    """
    class Meta:
        model = Donation
        fields = '__all__'

class RevenueShareSerializer(serializers.ModelSerializer):
    """
    Serializes RevenueShare objects for API input/output.
    Used for managing how revenue is split between platform and streamers.
    """
    class Meta:
        model = RevenueShare
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializes Transaction objects for API input/output.
    Used for managing financial transactions (donations, subscriptions, payouts, etc.).
    """
    class Meta:
        model = Transaction
        fields = '__all__'

class PayoutSerializer(serializers.ModelSerializer):
    """
    Serializes Payout objects for API input/output.
    Used for managing streamer payouts from the platform.
    """
    class Meta:
        model = Payout
        fields = '__all__'
