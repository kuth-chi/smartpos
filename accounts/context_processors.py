from django.conf import settings

def project_version():
    """
    Returns the project version.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        dict: A dictionary containing the project version.
    """
    return{
        'PROJECT_VERSION': settings.PROJECT_VERSION
    }