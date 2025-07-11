"""
chat/serializers.py

This module defines serializers for chat-related models, converting model instances to JSON for API responses
and validating incoming data for chat messages, emotes, commands, moderation rules, and bots.
"""

from rest_framework import serializers
from .models import ChatMessage, ChatEmote, ChatCommand, ChatModerationRule, ChatBot

class ChatMessageSerializer(serializers.ModelSerializer):
    """
    Serializes ChatMessage objects for API input/output.
    All fields are included for full chat message details.
    """
    class Meta:
        model = ChatMessage
        fields = '__all__'  # Includes all fields from the ChatMessage model

class ChatEmoteSerializer(serializers.ModelSerializer):
    """
    Serializes ChatEmote objects for API input/output.
    Used for uploading, listing, and managing emotes.
    """
    class Meta:
        model = ChatEmote
        fields = '__all__'

class ChatCommandSerializer(serializers.ModelSerializer):
    """
    Serializes ChatCommand objects for API input/output.
    Used for managing chat commands (e.g., !ban, !shoutout).
    """
    class Meta:
        model = ChatCommand
        fields = '__all__'

class ChatModerationRuleSerializer(serializers.ModelSerializer):
    """
    Serializes ChatModerationRule objects for API input/output.
    Used for managing moderation rules (e.g., banned words, spam detection).
    """
    class Meta:
        model = ChatModerationRule
        fields = '__all__'

class ChatBotSerializer(serializers.ModelSerializer):
    """
    Serializes ChatBot objects for API input/output.
    Used for managing chat bots that automate moderation or engagement.
    """
    class Meta:
        model = ChatBot
        fields = '__all__'
