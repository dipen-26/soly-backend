from rest_framework.test import APITestCase
from django.urls import reverse
from accounts.models import User
from streams.models import Stream
from content.models import Highlight

class ContentAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='contentapi@example.com', password='pass')
        self.stream = Stream.objects.create(title='API Content Stream', streamer=self.user, status='live')
        self.client.force_authenticate(user=self.user)

    def test_create_highlight(self):
        url = reverse('content:highlight-list')
        data = {'stream': self.stream.id, 'title': 'API Highlight'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Highlight.objects.count(), 1)
