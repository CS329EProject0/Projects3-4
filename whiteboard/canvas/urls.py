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
   url(r'register/', auth_views.login, {'template_name':'createAccount.html'}),
   url(r'login/', auth_views.login, {'template_name':'login.html'}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
