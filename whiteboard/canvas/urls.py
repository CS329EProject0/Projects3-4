#canvas/urls.py
from django.conf.urls import url
from canvas.views import *
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
import canvas.static as stc

urlpatterns = [
   url(r'^$', CanvasIndex.as_view(), name = "index"),
   #url(r'featured/', Featured.as_view()), #This is a broken url
   url(r'welcome/', WelcomeView.as_view(), name='welcome'),
   url(r'register/', UserFormView.as_view(), name="register"),
   url(r'login/', auth_views.login, {'template_name':'login.html'}),
   url(r'create_quiz/', QuizCreationView.as_view(),name='quizCreation')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
