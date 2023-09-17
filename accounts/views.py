from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import phonenumbers
from phonenumbers.phonenumberutil import is_valid_number

from .models import User
from .forms import UserRegisterForm


@login_required
def dashboard_user(request):
    return render(request, 'auth/dash/dashboard.html')


def is_phone_number(value):
    try:
        parsed_number = phonenumbers.parse(value, None)  # None means "use the default region"
        if is_valid_number(parsed_number):
            return value
    except phonenumbers.NumberParseException:
        pass   # Invalid phone number format

    return None


User = get_user_model()
def user_signup(request):
    if request.user.is_authenticated:
        # for authenticated user, send them to dashboard
        return redirect('dashboard')
    
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            input_value = form.cleaned_data['email']
            phone_or_email = is_phone_number(input_value)

            if phone_or_email and phone_or_email != str(User.objects.filter(pramary_phone=phone_or_email)):
                print(str(User.objects.filter(pramary_phone=phone_or_email)))
                # check if a phone number
                user = User(primary_phone=phone_or_email)
                # set email to blank if using phone number
                user.email= '' 
            else:
                try:
                    # Check if an email address
                    User.objects.filter(email=input_value)
                    raise ValidationError(_('Email already in user'))
                except User.DoesNotExist:
                    # It's neither a valid phone number nor an existing email, raise an error
                    raise ValidationError(_('Invalid email address or phone number'))
                
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            # Add message
            messages.success(request, _('Registration successful.'))
            # Redirect to success page
            redirect('dashboard') # redirect to dashboard

        else:
            # Add message for registration failure
            error_message = _("Invalid registration data. Please check the form for the following errors:")
            for field, errors in form.errors.items():
                error_message += f"\n{field}: {', '.join(errors)}"
            messages.error(request, error_message)
    
    else:
        form = UserRegisterForm()

    return render(request, 'auth/register.html', {'form': form})


# User login methods
def user_login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    elif request.method == 'POST':
        # Get the username and password from the POST request
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful
        if user is not None:
            # Log the user in and set a session variable
            login(request, user)
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
