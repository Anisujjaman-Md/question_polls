from asyncio import futures
from django.test import TestCase

# Create your tests here.
#Testing

import datetime
from django.utils import timezone
from .models import Question

class QuestionModelTest():
    def test_was_published_recently_with_future_question(self):
        """Test_was_publised_recently_with_future_question() return false pr question whose publication_date
        is in the future"""
        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(publication_date = time)
        self.assertIs(future_question.was_published_recently(),False)