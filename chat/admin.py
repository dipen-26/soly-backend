"""
chat/admin.py

This module customizes the Django admin interface for chat-related models.
It allows administrators to view, search, and filter chat messages, emotes, commands, moderation rules, and bots efficiently.
"""

from django.contrib import admin
from .models import ChatMessage, ChatEmote, ChatCommand, ChatModerationRule, ChatBot

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for ChatMessage objects.
    - list_display: Shows these fields in the chat message list view.
    - search_fields: Allows admin to search messages by user and content.
    - list_filter: Enables filtering by message type, moderation, and deletion status.
    """
    list_display = ('stream', 'user', 'message_type', 'created_at', 'is_moderated', 'is_deleted')
    search_fields = ('user__username', 'message')
    list_filter = ('message_type', 'is_moderated', 'is_deleted')

@admin.register(ChatEmote)
class ChatEmoteAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for ChatEmote objects.
    - list_display: Shows emote details.
    - search_fields: Allows admin to search emotes by streamer and name.
    - list_filter: Enables filtering by active and animated status.
    """
    list_display = ('streamer', 'name', 'is_animated', 'tier_required', 'is_active')
    search_fields = ('streamer__username', 'name')
    list_filter = ('is_active', 'is_animated')

@admin.register(ChatCommand)
class ChatCommandAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for ChatCommand objects.
    - list_display: Shows command details and usage stats.
    - search_fields: Allows admin to search commands by streamer and command name.
    - list_filter: Enables filtering by active status and user level.
    """
    list_display = ('streamer', 'command', 'cooldown', 'user_level', 'is_active', 'usage_count')
    search_fields = ('streamer__username', 'command')
    list_filter = ('is_active', 'user_level')

@admin.register(ChatModerationRule)
class ChatModerationRuleAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for ChatModerationRule objects.
    - list_display: Shows rule details and ML status.
    - search_fields: Allows admin to search rules by streamer and name.
    - list_filter: Enables filtering by active status, ML assistance, and rule type.
    """
    list_display = ('streamer', 'name', 'rule_type', 'action', 'is_active', 'ml_assisted')
    search_fields = ('streamer__username', 'name')
    list_filter = ('is_active', 'ml_assisted', 'rule_type')

@admin.register(ChatBot)
class ChatBotAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for ChatBot objects.
    - list_display: Shows bot details and ML usage.
    - search_fields: Allows admin to search bots by streamer and name.
    - list_filter: Enables filtering by active status and ML capabilities.
    """
    list_display = ('streamer', 'name', 'is_active', 'can_moderate', 'uses_ml')
    search_fields = ('streamer__username', 'name')
    list_filter = ('is_active', 'can_moderate', 'uses_ml')
