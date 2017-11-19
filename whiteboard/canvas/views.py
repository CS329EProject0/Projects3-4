from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader
from django.contrib.auth import authenticate,login
from django.views import generic

# Index page view
class CanvasIndex(View):

    template  = loader.get_template('index.html')

    def get(self):
        return HttpResponse(self.template.render())