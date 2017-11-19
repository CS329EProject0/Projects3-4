#canvas/urls.py
from django.conf.urls import url
from canvas.views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   url(r'^$', CanvasIndex.as_view(), name = "index"),
]
