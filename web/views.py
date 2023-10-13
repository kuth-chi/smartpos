from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import translation
from django.contrib.auth.decorators import login_required
from accounts.models import User, SettingUser, AccountGallery
from django.utils.translation import gettext_lazy as _
from accounts.utils import get_user_profile_image
import qrcode
from django.utils.html import escape

# Create your views here.
def index_view(request):
    """
    This function handles the rendering of the index.html template.
    
    Parameters:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: The rendered index.html template.
    """
    return render(request, 'index.html')


# USER DASHBOARD

def dashboard_user(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    else:
        context = {
            'title_page': _('Dashboard'),
            'header_title': _('Dashboard'),
        }
        
        return render(request, 'dash/dashboard.html', context)


def change_language(request, language_code):
    # Set the language for the user
    translation.activate(language_code)
    request.session[translation.LANGUAGE_SESSION_KEY] = language_code

    # Redirect to the previous page or a specific URL
    next_url = request.GET.get('next', None)
    if next_url:
        return HttpResponseRedirect(next_url)
    else:
        return HttpResponseRedirect(reverse('home'))  # Change 'home' to your desired URL name
    
    
#List of Profile
@login_required
def profile_list(request):
    try:
        profiles = User.objects.filter(is_public=True)
        cover_url = AccountGallery.objects.filter(uploaded_by=request.user.id, is_cover_set=True).first()
        if cover_url:
            cover_url = cover_url.image.url
        else:
            cover_url = "/static/img/no_image.jpg"
    except User.DoesNotExist:
        profiles = None
        cover_url = "/static/img/no_image.jpg"
    context = {
        'title_page': _('List of Profiles'),
        'header_title': _('List of Profiles'),
        'profiles': profiles,
        'cover_url': cover_url,
    }
    
    return render(request, 'web/profiles/list_profiles.html', context)
    



# Public Profile
def public_profile(request, user_uuid):
    
    
    user = get_object_or_404(User, uuid=user_uuid, is_public=True)
    try:
        cover_url = AccountGallery.objects.filter(uploaded_by=user.id, is_cover_set=True).first()
    except AccountGallery.DoesNotExist:
        cover_url = None

   
    
    user_settings = SettingUser.objects.filter(user=user.pk).first()
    is_first_name = user_settings.is_first_name if user_settings is not None else False
    # Check if the user has an avatar, and provide a default if not
    if user.avatar:
        avatar_url = user.avatar.url
    else:
        avatar_url = "/static/img/default_avatar.jpg"  # Replace with your default image path

    context = {
        'title_page': user.first_name + ' ' + user.last_name + ' Profile',
        'header_title': _('Public Profile'),
        'profile': user,
        'cover_url': cover_url,
        'setting_user': user_settings,
        'avatar_url': avatar_url,  # Include the avatar_url in your context
        'is_first_name': is_first_name
    }
    
    return render(request, 'web/profiles/profile.html', context)

# QR Code

def generate_vcard_qr(request, user_uuid):
    # Fetch the user data based on the user_uuid
    user = get_object_or_404(User, uuid=user_uuid, is_public=True)

    # Create a vCard string
    vcard_data = f"BEGIN:VCARD\n" \
                 f"VERSION:3.0\n" \
                 f"FN:{escape(user.get_full_name())}\n" \
                 f"ORG:{escape(user.organization)}\n" \
                 f"TEL;TYPE=work,voice:{escape(user.primary_phone)}\n" \
                 f"EMAIL:{escape(user.email)}\n" \
                 f"URL:{escape(user.website_url)}\n" \
                 f"END:VCARD"

    # Generate a QR code from the vCard data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Serve the QR code image as an HTTP response
    response = HttpResponse(content_type="image/png")
    qr_image.save(response, "PNG")
    return response




@login_required
def user_profile(request):
    username = User.objects.get(username=request.user.username)
    context = {
        'title_page': _('Home') + ': ' + str(username).upper() + ' Account Settings',
        'header_title': _('Account Settings'),
        
    }
    return render(request, 'accounts/profile.html', context)


# 404 
def page_not_found_view(request, exception):
    return render(request, 'web/404.html', status=404)
