from django.shortcuts import get_object_or_404
import phonenumbers
from phonenumbers.util import prnt
from .models import AccountGallery


# PROFILE IMAGE
def get_user_profile_image(user):
    profile_image = None
    account_gallery = get_object_or_404(AccountGallery, uploaded_by=user, is_avatar=True)
    if account_gallery.image:
        profile_image = account_gallery.image.url
    return profile_image


# Validate Phone number
def is_phone_number(value, is_email=False):
    if is_email:
        return value

    try:
        # None means "use the default region"
        parsed_number = phonenumbers.parse(value, None)
        if phonenumbers.is_valid_number(parsed_number):
            return value
    except phonenumbers.NumberParseException:
        pass  # Invalid phone number format

    return None
