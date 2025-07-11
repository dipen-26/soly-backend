"""
chat/urls.py

This module defines URL routes for the chat app, mapping API endpoints to their corresponding viewsets.
Uses Django REST Framework's router to automatically generate RESTful routes for chat features.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatMessageViewSet, ChatEmoteViewSet, ChatCommandViewSet, ChatModerationRuleViewSet, ChatBotViewSet

# Router automatically generates RESTful routes for each chat feature
router = DefaultRouter()
router.register(r'chat-messages', ChatMessageViewSet)
router.register(r'chat-emotes', ChatEmoteViewSet)
router.register(r'chat-commands', ChatCommandViewSet)
router.register(r'chat-moderation-rules', ChatModerationRuleViewSet)
router.register(r'chat-bots', ChatBotViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all chat API endpoints
]

# This file connects HTTP requests to the correct view logic for chat features.
