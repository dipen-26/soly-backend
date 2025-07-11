"""
Tests for the Analytics app of Soly - Live Streaming Platform.

This module covers:
- Model tests for StreamerAnalytics (basic creation and field validation)
- API tests for StreamerAnalytics endpoint (creation via REST API)

All tests use Django's built-in test framework and DRF's APITestCase for API endpoints.

Workflows:
- Model tests ensure that objects can be created and fields are set as expected.
- API tests simulate client requests to the REST API, checking for correct status codes and database changes.

Each test is isolated and uses a temporary test database.
"""

from django.test import TestCase
from analytics.models import StreamerAnalytics
from accounts.models import User
from rest_framework.test import APITestCase

class StreamerAnalyticsModelTest(TestCase):
    """
    Test creation and field assignment for StreamerAnalytics model.
    Workflow:
    - Create a test user
    - Create a StreamerAnalytics object for that user
    - Assert that the streamer field matches the user
    """
    def setUp(self):
        # Create a test user for analytics
        self.user = User.objects.create_user(username='analyticsuser', email='analyticsuser@example.com', password='pass')

    def test_create_analytics(self):
        # Create a StreamerAnalytics object for the test user
        analytics = StreamerAnalytics.objects.create(streamer=self.user)
        # Check that the streamer field is set correctly
        self.assertEqual(analytics.streamer, self.user)
        # This verifies that the model can store and retrieve basic relationships

class AnalyticsAPITest(APITestCase):
    """
    Test the StreamerAnalytics API endpoint for creating analytics records.
    Workflow:
    - Create and authenticate a test user
    - POST to the streamer-analytics endpoint with the user's ID
    - Assert that the response is successful and the record is created
    """
    def setUp(self):
        # Create a test user and authenticate for API requests
        self.user = User.objects.create_user(username='analyticsapi', email='analyticsapi@example.com', password='pass')
        self.client.force_authenticate(user=self.user)

    def test_create_analytics(self):
        # API endpoint for creating StreamerAnalytics
        url = '/api/analytics/streamer-analytics/'
        # Data payload: only streamer ID is required for basic creation
        data = {'streamer': self.user.id}
        # Send POST request to create analytics record
        response = self.client.post(url, data, format='json')
        # Check that the response status is 201 (created)
        self.assertEqual(response.status_code, 201)
        # Check that the record was actually created in the database
        self.assertEqual(StreamerAnalytics.objects.count(), 1)
        # This ensures the API endpoint works for basic analytics creation
