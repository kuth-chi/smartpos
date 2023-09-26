from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import HttpRequest

User = get_user_model()

class CustomUserModelBackend(ModelBackend):
    """
    A custom authentication backend for the Django user model.
    """
    def authenticate(self, request: HttpRequest, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            # Check if username is email, primary phone, or username
            user = user_model.objects.get(Q(email=username) | Q(primary_phone=username) | Q(username=username))
        except user_model.DoesNotExist:
            return None

        # Check if the request is secure (SSL) or not.
        if request.is_secure():
            # Enforce SSL-based authentication.
            if user.check_password(password):
                user.backend = f'{self.__module__}.{self.__class__.__name__}'  # Set the backend attribute
                return user
        else:
            # Non-SSL authentication (insecure).
            # You can add additional authentication logic here if needed.
            # For example, check passwords over HTTP without SSL, but be cautious as it's less secure.
            pass

        return None