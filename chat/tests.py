"""
chat/tests.py

This module contains tests for the chat app, covering chat message creation and chat API endpoints.
Tests help ensure that chat features work as expected for both users and streamers.
"""

from django.test import TestCase
from chat.models import ChatMessage
from accounts.models import User
from streams.models import Stream
from rest_framework.test import APITestCase

class ChatMessageModelTest(TestCase):
    """
    Tests for the ChatMessage model.
    Ensures that chat messages are created correctly and linked to users and streams.
    """
    def setUp(self):
        # Create a user and a stream for testing
        self.user = User.objects.create_user(username='chatuser', email='chatuser@example.com', password='pass')
        self.stream = Stream.objects.create(title='Chat Stream', streamer=self.user, category='General', tags=[])

    def test_create_message(self):
        # Create a chat message and verify its fields
        msg = ChatMessage.objects.create(user=self.user, stream=self.stream, message='Hello!')
        self.assertEqual(msg.message, 'Hello!')
        self.assertEqual(msg.user, self.user)
        self.assertEqual(msg.stream, self.stream)

class ChatAPITest(APITestCase):
    """
    Tests for chat API endpoints (sending messages).
    Ensures that authenticated users can send messages via the API and messages are stored correctly.
    """
    def setUp(self):
        # Create a user and a stream, and authenticate the user for API tests
        self.user = User.objects.create_user(username='chatapi', email='chatapi@example.com', password='pass')
        self.stream = Stream.objects.create(title='API Chat Stream', streamer=self.user, category='General', tags=[])
        self.client.force_authenticate(user=self.user)

    def test_send_message(self):
        # Simulate sending a chat message via the API
        url = '/api/chat/chat-messages/'
        data = {'stream': self.stream.id, 'user': self.user.id, 'message': 'API message'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  # Message should be created successfully
        self.assertEqual(ChatMessage.objects.count(), 1)  # One message should exist in the database
