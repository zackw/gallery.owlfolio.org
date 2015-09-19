from django.contrib.auth.models import User

from .models import AutoLogin

class TokenBackend(object):
    def authenticate(self, username=None, token=None):
        try:
            user = User.objects.get(username=username)
            matching_token = AutoLogin.objects.get(user=user, token=token)
        except (User.DoesNotExist, AutoLogin.DoesNotExist):
            return None
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None