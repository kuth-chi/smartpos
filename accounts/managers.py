from django.contrib.auth.models import BaseUserManager

class UserAccountManager(BaseUserManager):
    """
    Custom manager for the User model
    """
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, username, primary_phone, and password.
        """
        if not username:
            raise ValueError("Need to provide a username")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username, password, and extra fields.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, username, password=password, **extra_fields)
