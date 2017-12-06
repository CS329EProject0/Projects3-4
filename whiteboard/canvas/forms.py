from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

#This will handle form submissions throughout the application, the actual implementation is in the views.py file
class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','password']

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['bio']
#Create Assignment
class AssignmentForm(forms.ModelForm):

	class Meta:
		model = Assignment
		# implement file upload here
		fields = []

#Create Quest
class CreateQuestForm(forms.ModelForm):

	class Meta:
		model = Quest
		fields = ['requirements']


#Create Quiz
class CreateQuizForm(forms.ModelForm):

	class Meta:
		model = Quiz
		# figure out a way to add questions
		fields = []

#Take Quiz
class TakeQuizForm(forms.ModelForm):

	class Meta:
		model = Quiz
		fields = []

#If teacher ===== define set of skills