"""
content/tests.py

This module contains tests for the content app, covering highlight creation and content API endpoints.
Tests help ensure that content features work as expected for both users and streamers.
"""

from django.test import TestCase
from content.models import Highlight, VOD
from accounts.models import User
from streams.models import Stream
from rest_framework.test import APITestCase
from datetime import timedelta

class HighlightModelTest(TestCase):
    """
    Tests for the Highlight model.
    Ensures that highlights are created correctly and linked to VODs and users.
    """
    def setUp(self):
        # Create a user, stream, and VOD for testing
        self.user = User.objects.create_user(username='contentuser', email='contentuser@example.com', password='pass')
        self.stream = Stream.objects.create(title='Content Stream', streamer=self.user, category='General', tags=[])
        self.vod = VOD.objects.create(stream=self.stream, streamer=self.user, title='VOD', description='', duration=timedelta(minutes=10), view_count=0, video_url='http://example.com/vod.mp4', thumbnail='vod.jpg')

    def test_create_highlight(self):
        # Create a highlight and verify its fields
        highlight = Highlight.objects.create(vod=self.vod, title='Test Highlight', start_time=timedelta(), end_time=timedelta(minutes=1), duration=timedelta(minutes=1), created_by=self.user, highlight_score=0.9, content_type='gameplay')
        self.assertEqual(highlight.vod, self.vod)
        self.assertEqual(highlight.title, 'Test Highlight')

class ContentAPITest(APITestCase):
    """
    Tests for content API endpoints (creating highlights).
    Ensures that authenticated users can create highlights via the API and highlights are stored correctly.
    """
    def setUp(self):
        # Create a user, stream, and VOD, and authenticate the user for API tests
        self.user = User.objects.create_user(username='contentapi', email='contentapi@example.com', password='pass')
        self.stream = Stream.objects.create(title='API Content Stream', streamer=self.user, category='General', tags=[])
        self.vod = VOD.objects.create(stream=self.stream, streamer=self.user, title='VOD', description='', duration=timedelta(minutes=10), view_count=0, video_url='http://example.com/vod.mp4', thumbnail='vod.jpg')
        self.client.force_authenticate(user=self.user)

    def test_create_highlight(self):
        # Simulate creating a highlight via the API
        url = '/api/content/highlights/'
        data = {
            'vod': self.vod.id,
            'title': 'API Highlight',
            'start_time': '00:00:00',
            'end_time': '00:01:00',
            'duration': '00:01:00',
            'created_by': self.user.id,
            'highlight_score': 0.8,
            'content_type': 'gameplay'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  # Highlight should be created successfully
        self.assertEqual(Highlight.objects.count(), 1)  # One highlight should exist in the database
