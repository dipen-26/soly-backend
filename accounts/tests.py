"""
accounts/tests.py

This module contains tests for the accounts app, covering user model creation and authentication API endpoints.
Tests help ensure that user registration, login, and permissions work as expected.
"""

from django.test import TestCase
from accounts.models import User
from rest_framework.test import APITestCase
from django.urls import reverse

class UserModelTest(TestCase):
    """
    Tests for the custom User model.
    Ensures that users and superusers are created with correct attributes and password handling.
    """
    def test_create_user(self):
        # Create a regular user and check their email and password
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass'))  # Password should be hashed and verifiable
        self.assertFalse(user.is_staff)  # Regular users are not staff by default

    def test_create_superuser(self):
        # Create a superuser (admin) and check their privileges
        admin = User.objects.create_superuser(username='adminuser', email='admin@example.com', password='adminpass')
        self.assertTrue(admin.is_superuser)  # Superuser flag should be set
        self.assertTrue(admin.is_staff)  # Superusers are staff

class AuthAPITest(APITestCase):
    """
    Tests for authentication API endpoints (register and login).
    Ensures that users can register and log in via the API, and that tokens are returned on login.
    """
    def test_register(self):
        # Simulate user registration via API
        url = '/api/accounts/register/'
        data = {'username': 'apiuser', 'email': 'apiuser@example.com', 'password': 'apipass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)  # Registration should succeed
        self.assertTrue(User.objects.filter(email='apiuser@example.com').exists())  # User should be created

    def test_login(self):
        # Simulate user login via API
        User.objects.create_user(username='loginuser', email='login@example.com', password='loginpass')
        url = '/api/accounts/login/'
        data = {'username': 'loginuser', 'password': 'loginpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)  # Login should succeed
        self.assertIn('token', response.data)  # Token should be returned for authentication
