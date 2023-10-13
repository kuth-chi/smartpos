from django.shortcuts import get_object_or_404
from .models import AccountGallery
import phonenumbers



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



def get_user_profile_image(user):
    account_gallery = AccountGallery.objects.filter(uploaded_by=user, is_avatar=True).first()

    if account_gallery and account_gallery.image:
        return account_gallery.image.url
    return None
