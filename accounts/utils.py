import phonenumbers
from phonenumbers.util import prnt

# Validate Phone number



def is_phone_number(value, is_email=False):
    """
    Check if the given value is a valid phone number or email address.

    Parameters:
    - value: A string representing the phone number or email address to be validated.
    - is_email: A boolean indicating whether the value should be treated as an email address.

    Returns:
    - The input value if it is a valid phone number and is_email is False, or the input value if is_email is True, or None otherwise.
    """
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
