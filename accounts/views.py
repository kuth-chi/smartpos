from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import User
from .forms import UserRegisterForm
from .utils import is_phone_number
from django.db.models import Q



def dashboard_user(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    else:
        return render(request, 'auth/dash/index.html')


User = get_user_model()

def user_signup(request):
    if request.user.is_authenticated:
        # For an authenticated user, send them to the dashboard
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            input_value = form.cleaned_data['email']
            phone_or_email = is_phone_number(input_value, is_email=True)

            if phone_or_email:
                # The input value is an email address
                if User.objects.filter(email=phone_or_email).exists():
                    # Email address already in use
                    raise ValidationError(_('Email already in use'))
            else:
                # The input value is neither a valid phone number nor a valid email address
                raise ValidationError(_('Invalid email address or phone number'))

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Explicitly specify the authentication backend
            user = authenticate(request, username=user.email, password=form.cleaned_data['password1'], backend='accounts.authentication.CustomUserModelBackend')
            if user is not None:
                login(request, user)

            # Add a success message
            messages.success(request, _('Registration successful.'))
            # Redirect to the success page
            return redirect('dashboard')

        # Add a message for registration failure
        error_message = _("Invalid registration data. Please check the form for the following errors:")
        for field, errors in form.errors.items():
            error_message += f"\n{field}: {', '.join(errors)}"
        messages.error(request, error_message)

    else:
        form = UserRegisterForm()

    return render(request, 'auth/register.html', {'form': form})


# User login methods
from django.contrib.sessions.models import Session

def user_login(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    elif request.method == 'POST':
        # Get the username/email/primary_phone and password from the POST request
        username_or_email_or_phone = request.POST['username_or_email_or_phone']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me') == 'on'

        # Check if the input matches any of the user's username, email, or primary phone
        user = None
        try:
            user = User.objects.get(
                Q(username=username_or_email_or_phone) | 
                Q(email=username_or_email_or_phone) | 
                Q(primary_phone=username_or_email_or_phone)
            )
        except User.DoesNotExist:
            pass

        # Authenticate the user
        if user is not None and user.check_password(password):
            # Log the user in and set a session variable
            login(request, user, backend='accounts.authentication.CustomUserModelBackend')
            
            # Set session expiry based on 'remember me' checkbox
            if remember_me:
                request.session.set_expiry(0)  # Set session to never expire
            else:
                request.session.set_expiry(None)  # Use default session expiry time
            
            messages.success(request, "You have logged in successfully")
            # Redirect to a success page (replace 'dashboard' with your URL)
            return redirect('dashboard')
        else:
            # Authentication failed, show an error message
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'auth/login.html', {'error_message': error_message})

    # If it's a GET request, show the login form
    return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('user_login')
