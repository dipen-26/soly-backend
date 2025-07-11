from django.test import TestCase
from content.models import Highlight
from accounts.models import User
from streams.models import Stream

class HighlightModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='contentuser@example.com', password='pass')
        self.stream = Stream.objects.create(title='Content Stream', streamer=self.user, status='live')

    def test_create_highlight(self):
        highlight = Highlight.objects.create(stream=self.stream, title='Test Highlight')
        self.assertEqual(highlight.stream, self.stream)
        self.assertEqual(highlight.title, 'Test Highlight')
