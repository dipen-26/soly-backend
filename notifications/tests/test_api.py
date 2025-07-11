from rest_framework.test import APITestCase
from django.urls import reverse
from accounts.models import User
from notifications.models import Notification

class NotificationAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='notifyapi@example.com', password='pass')
        self.client.force_authenticate(user=self.user)

    def test_create_notification(self):
        url = reverse('notifications:notification-list')
        data = {'user': self.user.id, 'message': 'API notification'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Notification.objects.count(), 1)
