from django.test import TestCase
from chat.models import ChatMessage
from accounts.models import User
from streams.models import Stream

class ChatMessageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='chatuser', email='chatuser@example.com', password='pass')
        self.stream = Stream.objects.create(title='Chat Stream', streamer=self.user, category='General', tags=[])

    def test_create_message(self):
        msg = ChatMessage.objects.create(user=self.user, stream=self.stream, message='Hello!')
        self.assertEqual(msg.message, 'Hello!')
        self.assertEqual(msg.user, self.user)
        self.assertEqual(msg.stream, self.stream)
