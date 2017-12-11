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
   url(r'^assignments/$', AssignmentsView.as_view(),name='assignment'),
   url(r'^assignment/(?P<assignment_id>[0-9]+)/$', AssignmentView.as_view(), name='specific_assignment'),
   url(r'^createAssignment/$', CreateAssignmentView.as_view(), name = 'create_assignment'),
   url(r'^guild/$', GuildView.as_view(),name='guild'),
   url(r'^student_home/$', StudentHomeView.as_view(),name='student_home'),
   url(r'^teacher_home/$', TeacherHomeView.as_view(),name='teacher_home'),
   url(r'^quiz/$', QuizView.as_view(),name='quiz'),
   url(r'^create_quiz/$', CreateQuizView.as_view(),name='quizCreation')  
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
