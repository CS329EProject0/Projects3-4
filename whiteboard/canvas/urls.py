#canvas/urls.py
from django.conf.urls import url
from canvas.views import *
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   url(r'^$', CanvasIndex.as_view(), name = "index"),
   url(r'^welcome/$', WelcomeView.as_view(), name='welcome'),
   url(r'^register/$', UserFormView.as_view(), name="register"),
   url(r'^login/$', auth_views.login, {'template_name':'login.html'}, name = 'login'),
   url(r'^quest/$', QuestView.as_view(),name = 'quest'),
   url(r'^assignments/$', AssignmentsView.as_view(),name='assignments'),
   url(r'^assignment/(?P<assignment_id>[0-9]+)/$', AssignmentView.as_view(), name='specific_assignment'),
   url(r'^create_assignment/$', CreateAssignmentView.as_view(), name = 'create_assignment'),
   url(r'^guild/$', GuildView.as_view(),name='guild'),
   url(r'^student_home/$', StudentHomeView.as_view(),name='student_home'),
   url(r'^teacher_home/$', TeacherHomeView.as_view(),name='teacher_home'),
   url(r'^quizzes/$', QuizzesView.as_view(),name='quizzes'),
   url(r'^quiz/(?P<quiz_id>[0-9]+)/$', QuizView.as_view(), name='specific_quiz'),
   url(r'^edit_quiz/(?P<quiz_id>[0-9]+)/', EditQuizView.as_view(), name='edit_quiz'),
   url(r'^edit_quizzes/$', EditQuizzesView.as_view(),name='edit_quizzes'),
   url(r'^update_question/(?P<question_id>[0-9]+)/', UpdateQuestionView.as_view(), name='update_question'),
   url(r'^create_quiz/$', CreateQuizView.as_view(),name='create_quiz'),
   url(r'^teacher_reports/$', TeacherReportsView.as_view(),name='teacher_reports'),
   url(r'^student_report/$', StudentReportView.as_view(),name='student_report')  
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
