"""
streams/tests.py

This module contains tests for the streams app, covering stream creation and streaming API endpoints.
Tests help ensure that streaming features work as expected for both users and streamers.
"""

from django.test import TestCase
from streams.models import Stream
from accounts.models import User
from rest_framework.test import APITestCase

class StreamModelTest(TestCase):
    """
    Tests for the Stream model.
    Ensures that streams are created correctly and linked to users.
    """
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='streamer', email='streamer@example.com', password='pass')

    def test_create_stream(self):
        # Create a stream and verify its fields
        stream = Stream.objects.create(
            title='Test Stream',
            streamer=self.user,
            category='Gaming',
            tags=[],
        )
        self.assertEqual(stream.title, 'Test Stream')
        self.assertEqual(stream.streamer, self.user)

class StreamAPITest(APITestCase):
    """
    Tests for streaming API endpoints (creating streams).
    Ensures that authenticated users can create streams via the API and streams are stored correctly.
    """
    def setUp(self):
        # Create a user and authenticate for API tests
        self.user = User.objects.create_user(username='streamer2', email='streamer2@example.com', password='pass')
        self.client.force_authenticate(user=self.user)

    def test_create_stream(self):
        # Simulate creating a stream via the API
        url = '/api/streams/streams/'
        data = {'title': 'API Stream', 'streamer': self.user.id, 'category': 'Gaming', 'tags': []}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  # Stream should be created successfully
        self.assertEqual(Stream.objects.count(), 1)  # One stream should exist in the database
