"""
notifications/tests.py

This module contains tests for the notifications app, covering notification creation and notification API endpoints.
Tests help ensure that notification features work as expected for both users and streamers.
"""

from django.test import TestCase
from notifications.models import Notification
from accounts.models import User
from rest_framework.test import APITestCase

class NotificationModelTest(TestCase):
    """
    Tests for the Notification model.
    Ensures that notifications are created correctly and linked to users.
    """
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='notifyuser', email='notifyuser@example.com', password='pass')

    def test_create_notification(self):
        # Create a notification and verify its fields
        notif = Notification.objects.create(user=self.user, title='Test', message='Test notification', notification_type='test')
        self.assertEqual(notif.user, self.user)
        self.assertEqual(notif.message, 'Test notification')

class NotificationAPITest(APITestCase):
    """
    Tests for notification API endpoints (creating notifications).
    Ensures that authenticated users can create notifications via the API and notifications are stored correctly.
    """
    def setUp(self):
        # Create a user and authenticate for API tests
        self.user = User.objects.create_user(username='notifyapi', email='notifyapi@example.com', password='pass')
        self.client.force_authenticate(user=self.user)

    def test_create_notification(self):
        # Simulate creating a notification via the API
        url = '/api/notifications/notifications/'
        data = {'user': self.user.id, 'title': 'API', 'message': 'API notification', 'notification_type': 'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  # Notification should be created successfully
        self.assertEqual(Notification.objects.count(), 1)  # One notification should exist in the database
