from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import User
from .forms import UserRegisterForm
from .utils import is_phone_number


@login_required
def dashboard_user(request):
    return render(request, 'auth/dash/index.html')


User = get_user_model()
def user_signup(request):
    """
    Handle user sign up.
    ...
    """

    if request.user.is_authenticated:
        # for authenticated user, send them to dashboard
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
            login(request, user)
            # Add message
            messages.success(request, _('Registration successful.'))
            # Redirect to success page
            return redirect('dashboard')  # redirect to dashboard

        # Add message for registration failure
        error_message = _(
            "Invalid registration data. Please check the form for the following errors:")
        for field, errors in form.errors.items():
            error_message += f"\n{field}: {', '.join(errors)}"
        messages.error(request, error_message)

    else:
        form = UserRegisterForm()

    return render(request, 'auth/register.html', {'form': form})


# User login methods
from django.contrib.sessions.models import Session

def user_login(request):
    """
    Logs in a user.

    This function takes a request object as a parameter and checks if the user is already authenticated. If the user is authenticated, it redirects them to the dashboard page. If the user is not authenticated, it checks if the request method is POST and authenticates the user based on the provided username and password. 

    Parameters:
    - request: The request object containing the user's login information.

    Returns:
    - Redirects to the dashboard page if the user is authenticated.
    - Renders the login page if the user is not authenticated or the request method is not POST.
    """
    # Function implementation...

    if request.user.is_authenticated:
        return redirect('dashboard')

    elif request.method == 'POST':
        # Get the username and password from the POST request
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me') == 'on'

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful
        if user is not None:
            # Log the user in and set a session variable
            login(request, user)
            
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
