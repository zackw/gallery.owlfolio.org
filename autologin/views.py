from django.conf import settings
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login

def autologin(request, username, token):
    user = authenticate(username=username, token=token)
    try:
        next = request.GET['next']
    except KeyError:
        next = '/'
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect(next)
    else:
        return HttpResponseRedirect(settings.LOGIN_URL)