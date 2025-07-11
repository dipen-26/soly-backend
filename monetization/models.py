"""
monetization/models.py

This module defines the database models for the monetization system, including subscriptions, channel points, rewards, donations, revenue sharing, transactions, and payouts.
Models represent the structure of financial and engagement data, supporting ML analysis, payment workflows, and user incentives.
"""

from django.db import models
from django.conf import settings
from decimal import Decimal

class Subscription(models.Model):
    """
    Stores channel subscription details for users subscribing to streamers.
    Includes fields for payment, subscription status, ML churn risk, and lifetime value prediction.
    """
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )  # The user who subscribes
    streamer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscribers'
    )  # The streamer being subscribed to
    tier = models.PositiveSmallIntegerField()  # Subscription tier (1, 2, or 3)
    status = models.CharField(max_length=20)  # Subscription status (active, cancelled, expired)
    auto_renew = models.BooleanField(default=True)  # Whether subscription auto-renews
    
    # Subscription Details
    started_at = models.DateTimeField(auto_now_add=True)  # When subscription started
    current_period_start = models.DateTimeField()  # Start of current billing period
    current_period_end = models.DateTimeField()  # End of current billing period
    cancelled_at = models.DateTimeField(null=True, blank=True)  # When subscription was cancelled
    
    # Payment Information
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount paid per period
    currency = models.CharField(max_length=3, default='USD')  # Currency code
    payment_method = models.CharField(max_length=50)  # Payment method (e.g., card, PayPal)
    
    # ML/DL Fields
    churn_risk = models.FloatField(null=True)  # ML-predicted risk of cancellation
    lifetime_value = models.FloatField(null=True)  # Predicted lifetime value of the subscriber
    
    class Meta:
        unique_together = ('subscriber', 'streamer')  # Each user can only subscribe once per streamer
        indexes = [
            models.Index(fields=['streamer', 'status']),  # For fast lookup by streamer and status
            models.Index(fields=['current_period_end'])   # For fast lookup by period end
        ]

class ChannelPoints(models.Model):
    """
    Stores channel points for users, which can be earned and spent on rewards.
    Points encourage engagement and can be used for incentives.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The user earning/spending points
    streamer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='channel_points_streamer'
    )  # The streamer whose channel points are being managed
    points_balance = models.PositiveIntegerField(default=0)  # Current points balance
    total_earned = models.PositiveIntegerField(default=0)  # Total points earned
    total_spent = models.PositiveIntegerField(default=0)  # Total points spent
    last_earned = models.DateTimeField(null=True, blank=True)  # Last time points were earned
    
    # ML/DL Fields
    engagement_score = models.FloatField(default=0.0)  # User engagement level
    reward_preferences = models.JSONField(default=list)  # ML-predicted preferred rewards
    
    class Meta:
        unique_together = ('user', 'streamer')

class PointsReward(models.Model):
    """
    Model for channel points rewards
    """
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_auto_fulfill = models.BooleanField(default=False)
    max_per_stream = models.PositiveIntegerField(null=True)
    max_per_user_per_stream = models.PositiveIntegerField(null=True)
    cooldown = models.DurationField(null=True)
    
    # ML/DL Fields
    popularity_score = models.FloatField(default=0.0)  # ML-calculated popularity
    recommended_cost = models.PositiveIntegerField(null=True)  # ML-suggested optimal cost
    user_segments = models.JSONField(default=list)  # Target user segments

class Donation(models.Model):
    """
    Model for donations/tips
    """
    donor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='donations_sent'
    )
    streamer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='donations_received'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    message = models.TextField(blank=True)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Payment Status
    status = models.CharField(max_length=20)  # pending, completed, failed, refunded
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, unique=True)
    
    # ML/DL Fields
    sentiment_score = models.FloatField(null=True)  # Sentiment analysis of message
    fraud_score = models.FloatField(null=True)  # ML-detected fraud probability

class RevenueShare(models.Model):
    """
    Model for revenue sharing configuration
    """
    streamer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Revenue Share Percentages (stored as integers, e.g., 70 for 70%)
    subscription_share = models.PositiveSmallIntegerField(default=70)
    bits_share = models.PositiveSmallIntegerField(default=70)
    donation_share = models.PositiveSmallIntegerField(default=95)
    
    # Partnership Status
    partnership_level = models.PositiveSmallIntegerField(default=0)
    partnership_start_date = models.DateField(null=True)
    
    # Payment Information
    payment_method = models.CharField(max_length=50)
    payment_details = models.JSONField(default=dict)
    minimum_payout = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('100.00'))
    
    # ML/DL Fields
    revenue_prediction = models.JSONField(default=dict)  # Monthly revenue predictions
    growth_trajectory = models.JSONField(default=dict)  # Predicted growth metrics

class Transaction(models.Model):
    """
    Model for financial transactions
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50)  # subscription, donation, bits, etc.
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    
    # Related Models
    subscription = models.ForeignKey(Subscription, null=True, on_delete=models.SET_NULL)
    donation = models.ForeignKey(Donation, null=True, on_delete=models.SET_NULL)
    
    # Payment Processing
    payment_method = models.CharField(max_length=50)
    payment_provider = models.CharField(max_length=50)
    provider_transaction_id = models.CharField(max_length=100)
    
    # ML/DL Fields
    fraud_score = models.FloatField(null=True)  # ML-detected fraud probability
    risk_factors = models.JSONField(default=list)  # Identified risk factors
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'created_at']),
            models.Index(fields=['status', 'created_at'])
        ]

class Payout(models.Model):
    """
    Model for streamer payouts
    """
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    status = models.CharField(max_length=20)  # pending, processing, completed, failed
    payout_method = models.CharField(max_length=50)
    
    # Period Information
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()
    requested_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True)
    
    # Earnings Breakdown
    earnings_breakdown = models.JSONField(default=dict)  # Detailed earnings by source
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    
    # ML/DL Fields
    anomaly_score = models.FloatField(null=True)  # ML-detected payment anomalies
    verification_status = models.CharField(max_length=20, default='pending')
    
    class Meta:
        indexes = [
            models.Index(fields=['streamer', 'status']),
            models.Index(fields=['period_start', 'period_end'])
        ]
