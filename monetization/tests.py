"""
monetization/tests.py

This module contains tests for the monetization app, covering transaction creation and monetization API endpoints.
Tests help ensure that financial features work as expected for both users and streamers.
"""

from django.test import TestCase
from monetization.models import Transaction
from accounts.models import User
from rest_framework.test import APITestCase
from decimal import Decimal

class TransactionModelTest(TestCase):
    """
    Tests for the Transaction model.
    Ensures that transactions are created correctly and linked to users.
    """
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='moneyuser', email='moneyuser@example.com', password='pass')

    def test_create_transaction(self):
        # Create a transaction and verify its fields
        txn = Transaction.objects.create(user=self.user, transaction_type='donation', amount=Decimal('10.0'), currency='USD', status='completed', payment_method='card', payment_provider='stripe', provider_transaction_id='abc123')
        self.assertEqual(txn.user, self.user)
        self.assertEqual(txn.amount, Decimal('10.0'))
        self.assertEqual(txn.transaction_type, 'donation')

class MonetizationAPITest(APITestCase):
    """
    Tests for monetization API endpoints (creating transactions).
    Ensures that authenticated users can create transactions via the API and transactions are stored correctly.
    """
    def setUp(self):
        # Create a user and authenticate for API tests
        self.user = User.objects.create_user(username='moneyapi', email='moneyapi@example.com', password='pass')
        self.client.force_authenticate(user=self.user)

    def test_create_transaction(self):
        # Simulate creating a transaction via the API
        url = '/api/monetization/transactions/'
        data = {
            'user': self.user.id,
            'transaction_type': 'donation',
            'amount': '5.0',
            'currency': 'USD',
            'status': 'completed',
            'payment_method': 'card',
            'payment_provider': 'stripe',
            'provider_transaction_id': 'xyz789'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  # Transaction should be created successfully
        self.assertEqual(Transaction.objects.count(), 1)  # One transaction should exist in the database
