from django.test import TestCase
from surveys.models import Answer, Test, Choice, Question
from surveys.serializers import AnswerSerializer

from datetime import datetime


class TestSerializers():
    def setUp(self):
        Test.objects.create(
            test_name='name',
            date_start=datetime(2010, 1, 1, 0, 0, 0),
            date_end = datetime(2010, 1, 1, 0, 0, 0),
            test_description ="test description"
        )
        Question.objects.create(
            question_text = 'text question',
            question_type = 'many',
        )
        Choice.objects.create(
            choice_text = 'choice_text', 
        )
        Answer.objects.create(
            user_id=1,
            choice_text="test answer"
        )

    def test_answerSerializer(self):
         lion = Question.objects.get(name="test")

