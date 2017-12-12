from django.test import TestCase
from canvas.models import *
from views import TakeQuizView as quiz
# Create your tests here.
class DatabaseTests(TestCase):

	def setUp(self):
		Quest.objects.create(quest_id = 1, requirements= 1)
		Quest.objects.create(quest_id=2, requirements=100)

		Quiz.objects.create(quiz_id = 1,quest_id = 1)
		Quiz.objects.create(quiz_id=2, quest_id=2)

		Question.objects.create(question_id = 1,quiz_id =1,body = "Body for question 1",answer="Answer for question 1")
		Question.objects.create(question_id = 2,quiz_id =1,body = "Body for question 2",answer="Answer for question 2")
		Question.objects.create(question_id=3, quiz_id=2, body="Body for question 3", answer="Answer for question 3")
		Question.objects.create(question_id=4, quiz_id=2, body="Body for question 4", answer="Answer for question 4")

		Skill.objects.create(name = "Skill 1")
		Skill.objects.create(name="Skill 2")

	def query(self):
		pass

class ViewTests(TestCase):

	def testGrade(self):
		pass