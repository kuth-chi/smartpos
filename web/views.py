from django.shortcuts import render

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