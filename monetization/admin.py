"""
monetization/admin.py

This module customizes the Django admin interface for monetization-related models.
It allows administrators to view, search, and filter subscriptions, points, rewards, donations, revenue sharing, transactions, and payouts efficiently.
"""

from django.contrib import admin
from .models import Subscription, ChannelPoints, PointsReward, Donation, RevenueShare, Transaction, Payout

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for Subscription objects.
    - list_display: Shows these fields in the subscription list view.
    - search_fields: Allows admin to search subscriptions by subscriber and streamer.
    - list_filter: Enables filtering by status and tier.
    """
    list_display = ('subscriber', 'streamer', 'tier', 'status', 'started_at', 'current_period_end')
    search_fields = ('subscriber__username', 'streamer__username')
    list_filter = ('status', 'tier')

@admin.register(ChannelPoints)
class ChannelPointsAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for ChannelPoints objects.
    - list_display: Shows points details and balances.
    - search_fields: Allows admin to search points by user and streamer.
    """
    list_display = ('user', 'streamer', 'points_balance', 'total_earned', 'total_spent', 'last_earned')
    search_fields = ('user__username', 'streamer__username')

@admin.register(PointsReward)
class PointsRewardAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for PointsReward objects.
    - list_display: Shows reward details and status.
    - search_fields: Allows admin to search rewards by streamer and title.
    - list_filter: Enables filtering by active status.
    """
    list_display = ('streamer', 'title', 'cost', 'is_active', 'is_auto_fulfill')
    search_fields = ('streamer__username', 'title')
    list_filter = ('is_active',)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for Donation objects.
    - list_display: Shows donation details and status.
    - search_fields: Allows admin to search donations by donor and streamer.
    - list_filter: Enables filtering by status and currency.
    """
    list_display = ('donor', 'streamer', 'amount', 'currency', 'status', 'created_at')
    search_fields = ('donor__username', 'streamer__username')
    list_filter = ('status', 'currency')

@admin.register(RevenueShare)
class RevenueShareAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for RevenueShare objects.
    - list_display: Shows revenue share details and partnership level.
    - search_fields: Allows admin to search revenue shares by streamer.
    """
    list_display = ('streamer', 'subscription_share', 'bits_share', 'donation_share', 'partnership_level')
    search_fields = ('streamer__username',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for Transaction objects.
    - list_display: Shows transaction details and status.
    - search_fields: Allows admin to search transactions by user and type.
    - list_filter: Enables filtering by status and transaction type.
    """
    list_display = ('user', 'transaction_type', 'amount', 'currency', 'status', 'created_at')
    search_fields = ('user__username', 'transaction_type')
    list_filter = ('status', 'transaction_type')

@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for Payout objects.
    - list_display: Shows payout details and status.
    - search_fields: Allows admin to search payouts by streamer.
    - list_filter: Enables filtering by status and currency.
    """
    list_display = ('streamer', 'amount', 'currency', 'status', 'period_start', 'period_end', 'requested_at')
    search_fields = ('streamer__username',)
    list_filter = ('status', 'currency')
