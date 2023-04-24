from .models import CustomUser as User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404


class AuthBackend(object):

    def authenticate(self, request, username=None, password=None):
        
        user = get_object_or_404(User, email=username)
        match_password = check_password(password, user.password)
        print(match_password)
        if user and match_password:
            return user
        else:
            return None
       

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None