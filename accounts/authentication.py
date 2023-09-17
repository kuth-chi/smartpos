from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class CustomUserModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Check if username is email, primary phone, or username
            user = UserModel.objects.get(Q(email=username) | Q(primary_phone=username) | Q(username=username))
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
