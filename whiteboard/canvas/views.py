from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views import generic
import random

#The majority of everything will go in here

# Index page view
class CanvasIndex(View):

    template  = loader.get_template('index.html')
    def get(self, request):
        return HttpResponse(self.template.render())

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    foo = random.randint(0,100)
    user.bio = "Some words plus the random number: {}".format(str(foo))
    user.save()

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