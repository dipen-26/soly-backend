from rest_framework.test import APITestCase
from accounts.models import User
from streams.models import Stream
from chat.models import ChatMessage

class ChatAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='chatapi', email='chatapi@example.com', password='pass')
        self.stream = Stream.objects.create(title='API Chat Stream', streamer=self.user, category='General', tags=[])
        self.client.force_authenticate(user=self.user)

    def test_send_message(self):
        url = '/api/chat/chat-messages/'
        data = {'stream': self.stream.id, 'user': self.user.id, 'message': 'API message'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ChatMessage.objects.count(), 1)
