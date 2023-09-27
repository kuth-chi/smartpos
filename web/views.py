from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import translation

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
