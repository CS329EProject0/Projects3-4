from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views import generic
from .forms import *
import random

#The majority of everything will go in here
class UserFormView(View):
	form_class_main= UserForm
	form_class_student = StudentForm
	template = loader.get_template("createAccount.html")

	def get(self,request):
		form_main= self.form_class_main(None)
		form_student = self.form_class_student(None)
		return render(request, "createAccount.html", {'form_main':form_main,'form_student':form_student})

	#To get form data
	def post(self,request):
		form_main= self.form_class_main(request.POST)
		form_student = self.form_class_student(request.POST)

		print("Checking valid")
		if form_main.is_valid() and form_student.is_valid():
			print("Valid!")
			user = form_main.save(commit=False)
			user.credentials = form_student.save(commit=False)

			#This creates a temporary form user to recieve input from the forms

			#user.refresh_from_db()
			# This part is to clean the data, not necessary, but pretty common practice
			user.set_password(form_main.cleaned_data.get('password1'))
			user.save()
			user.credentials.save()
			#This is where the auth_user object is created, for the purposes of saving to the database
			print(user.username)
			print(user.password)
			print(user.credentials.is_teacher)
			user = authenticate(request, username=user.username, password=form_main.cleaned_data.get('password1'))
			print(user)
			print(user.credentials)
			#This "logs in" the user
			if user is not None:
				if user.is_active:
					login(request,user)
					print("Redirecting..............")
					return HttpResponseRedirect('/')
			else:
				#If it fails will display message
				print("Registration failed.............")
				#messages.add_message(request, 30, "Registration Failed")

		print("Not valid")
		return render(request, "createAccount.html", {'form_main':form_main, 'form_student':form_student})

class UserLoginFormView(View):
	form_class = UserLoginForm
	template = loader.get_template("login.html")

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			# This creates a temporary form user to recieve input from the forms
			user = form.save(commit=False)

			# This part is to clean the data, not necessary, but pretty common practice
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			# This is where the auth_user object is created, for the purposes of saving to the database
			user = authenticate(request, username=username, password=password)

			# This "logs in" the user
			if user is not None:
				if user.is_active:
					login(request, user)
					print("Redirecting..............")
					return HttpResponseRedirect('/welcome')
			else:
				# If it fails will display message
				print("Login failed.............")
				#messages.add_message(request, 30, "Login Failed")

		return render(request, "login.html", {'form': form})

# Index page view
class CanvasIndex(View):

	template  = loader.get_template('index.html')
	def get(self, request):
		context_dict = {"user":request.user}
		return HttpResponse(self.template.render(context=context_dict))


class WelcomeView(View):

	template = loader.get_template('Welcome.html')
	def get(self, request):
		context_dict = {"user": request.user}
		if not request.user.is_anonymous():
			if(request.user.credentials.is_teacher):
				return HttpResponseRedirect('/teacher_home')
			else:
				return HttpResponseRedirect('/student_home')
		return HttpResponse(self.template.render(context=context_dict))


class CreateQuizView(View):

	template = loader.get_template('CreateQuiz.html')
	def get(self, request):
		return HttpResponse(self.template.render())


class QuizView(View):

	template = loader.get_template('Quiz.html')
	def get(self, request):
		return HttpResponse(self.template.render())


class CreateAssignmentView(View):

	form_main = CreateAssignmentForm
	template = loader.get_template('CreateAssignment.html')

	def post(self, request):
		form_main = AssignmentForm(request.POST)

		if form_main.is_valid():
			description = form_main.cleaned_data['description']
			newAssignment = Assignment(description = description).save()
			return HttpResponseRedirect('/createAssignment/')

	def get(self, request):
		form_main_instance = self.form_main()
		return render(request, "CreateAssignment.html", {"form_main": form_main_instance})


class AssignmentView(View):

	# the additional variable, in this case assignment_id, is passed into the function
	# when a url request is made. The variable, assigment_id, is grabbed from the url
	# request as designnated in the urls.py file
	def get(self, request, assignment_id):

		# try to grab the appropriate assignment with its id
		try:
			assignment_specific = Assignment.objects.get(pk = assignment_id)
		except Assignment.DoesNotExist:
			raise Http404("Assignment does not exist.")

		# return the template with the assignment object passed into it, in this case
		# we are calling the object "assigment_specific"
		# this variable will now be able to be used in the Assigment.html template
		return render(request, 'Assignment.html', {'assignment_specific':assignment_specific, 'assignment_id':assignment_id})




class QuestView(View):

	template = loader.get_template('Quest.html')
	def get(self, request):
		return HttpResponse(self.template.render())


class StudentHomeView(View):

	template = loader.get_template('StudentHome.html')
	def get(self, request):
		return HttpResponse(self.template.render())

class TeacherHomeView(View):

	template = loader.get_template('TeacherHome.html')
	def get(self, request):
		return HttpResponse(self.template.render())

class GuildView(View):

	template = loader.get_template('Guild.html')
	def get(self, request):
		return HttpResponse(self.template.render())



#@login_required
#@transaction.atomic
"""def update_profile(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, _('Your profile was successfully updated!'))
			return redirect('settings:profile')
		else:
			messages.error(request, _('Please correct the error below.'))
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
	return render(request, 'profiles/profile.html', {
		'user_form': user_form,
		'profile_form': profile_form
	})
"""