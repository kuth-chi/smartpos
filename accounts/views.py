from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import User, SettingUser, UserAddress, AlternativePhone, UserSocial
from .forms import UserRegisterForm
from .utils import is_phone_number
from django.db.models import Q


# Create User Address
@login_required
def user_address_list(request, user_uuid):
    user = request.user
    user_address = get_object_or_404(UserAddress, user=user.id)
    context = {
        'title_page': _('Address List'),
        'header_title': _('Address List'),
        'user_address': user_address
    }
    return render(request, 'accounts/pages/addresses/list.html', context)

@login_required
def create_user_address(request, user_uuid):
    user_uuid =request.user.uuid

    context = {
        'title_page': _('Create New Address'),
        'header_title': _('Create New Address'),
    }
    
    return render(request, 'accounts/pages/addresses/create.html', context)


@login_required
def user_profile(request):
    user = request.user
    settings = SettingUser.objects.filter(user=user).first()
    addresses = UserAddress.objects.filter(user=user).first()
    alt_phones = AlternativePhone.objects.filter(user=user)
    social_profiles = UserSocial.objects.filter(user=user)

    context = {
        'user': user,
        'title_page': user.first_name + ' ' + user.last_name + ' - ' + _('Profile'),
        'header_title': _('Profile'),
        'setting_user': settings,
        'address': addresses,
        'alternative_phones': alt_phones,
        'social_profiles': social_profiles
    }
    return render(request, 'accounts/pages/profile.html', context)



User = get_user_model()
def user_signup(request):
    if request.user.is_authenticated:
        # For an authenticated user, send them to the dashboard
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            input_value = form.cleaned_data['email']
            phone_or_email = is_phone_number(input_value, is_email=True)

            if phone_or_email:
                # The input value is an email address
                if User.objects.filter(email=phone_or_email).exists():
                    # Email address already in use in the "accounts" database
                    raise ValidationError(_('Email already in use'))
            else:
                # The input value is neither a valid phone number nor a valid email address
                raise ValidationError(_('Invalid email address or phone number'))

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()  # Specify the database as 'accounts'

            # Explicitly specify the authentication backend
            user = authenticate(request, username=user.email, password=form.cleaned_data['password1'], backend='accounts.authentication.CustomUserModelBackend')
            if user is not None:
                login(request, user)

            # Add a success message
            messages.success(request, _('Registration successful.'))
            # Redirect to the success page
            return redirect('accounts:profile')

        # Add a message for registration failure
        error_message = _("Invalid registration data. Please check the form for the following errors:")
        for field, errors in form.errors.items():
            error_message += f"\n{field}: {', '.join(errors)}"
        messages.error(request, error_message)

    else:
        form = UserRegisterForm()

    return render(request, 'auth/register.html', {'form': form})



# User login methods
def user_login(request):
    # Check for the reference URL in the session
    reference_url = request.session.get('reference_url')
    if reference_url:
        request.session.pop('reference_url')
        return redirect(reference_url)
    
    if request.user.is_authenticated:
        # Redirect to a default page (e.g., the user's profile)
        return redirect('accounts:profile')

    if request.method == 'POST':
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

            # Check for the reference URL in the session again
            reference_url = request.session.get('reference_url')
            if reference_url:
                request.session.pop('reference_url')
                return redirect(reference_url)
            else:
                return redirect(reverse('accounts:profile'))
        else:
            # Authentication failed, show an error message
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'auth/login.html', {'error_message': error_message})

    # If it's a GET request, show the login form
    return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('accounts:login')
