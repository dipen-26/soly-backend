from django.test import TestCase
from notifications.models import Notification
from accounts.models import User

class NotificationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='notifyuser@example.com', password='pass')

    def test_create_notification(self):
        notif = Notification.objects.create(user=self.user, message='Test notification')
        self.assertEqual(notif.user, self.user)
        self.assertEqual(notif.message, 'Test notification')
