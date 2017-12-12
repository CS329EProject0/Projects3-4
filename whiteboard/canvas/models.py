from django.db import models
from django.utils import *
from django.contrib.auth.models import *
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.
SKILLS = (
        ('Accounting', 'Accounting'),
        ('Graphs', 'Graphs'),
        ('Calculus', 'Calculus'),
        ('Terms', 'Terms'),
        ('Logic', 'Logic'),
        ('Analysis', 'Analysis')
    )

#When created like this, in order to find the skill points for a question
#we query SkillPoints by question

#How to calculate score: Query skill points by question id

#A script will populate DB with skills list
class Skill(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return str(self.name)

class Quest(models.Model):
    requirements = models.IntegerField(default = 0)
    quest_id = models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.quest_id) + ": " + str(self.requirements)

class Quiz(models.Model):
    quiz_id = models.IntegerField(primary_key=True)
    quest_id = models.ForeignKey(Quest, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.quiz_id)

class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    quiz_id = models.ForeignKey(Quiz, null=True, on_delete=models.CASCADE)
    body = models.CharField(max_length=280)
    answer = models.CharField(max_length=50)
    def __str__(self):
        return str(self.body) + "\n\n" + str(self.answer)

class Assignment(models.Model):
    assignment_id = models.IntegerField(primary_key=True)
    quest_id = models.ForeignKey(Quest, null=True,on_delete=models.CASCADE)
    description = models.CharField(null = True, max_length = 500)
    file = models.FileField(null = True)
    def __str__(self):
        return str(self.assignment_id)

class Part(models.Model):
    part_id = models.IntegerField(primary_key=True)
    assigment_id = models.ForeignKey(Assignment,null = True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.part_id) + str(self.assigment_id)

class SkillPoints(models.Model):
    skill = models.ForeignKey(Skill,null=True, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,null=True,on_delete=models.CASCADE)
    part = models.ForeignKey(Part,null=True, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    def __str__(self):
        return str(self.skill) + str(self.points)

class Score(models.Model):
    student_id = models.IntegerField(primary_key=True)
    quiz_id = models.ForeignKey(Quiz,null=True, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(Assignment,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    is_teacher = models.BooleanField(default=False)
    bio = models.CharField(max_length=100,default="No bio")

class Guild(models.Model):
    guild_id = models.IntegerField(primary_key=True)
    students = models.ManyToManyField(Student)
    def __str__(self):
        return str(self.guild_id)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
    instance.student.save()