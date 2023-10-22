from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Organization

# Create your views here.
def OrganizationIndexView(request, pk):
    # Ensure the user has the appropriate permissions to access this view
    # For example, you can check if the logged-in user's ID matches the `pk`.
    if request.user.id != pk:
        return HttpResponseForbidden("You do not have permission to access this page.")

    own_organizations = Organization.objects.filter(user_id=pk).order_by('-created_at')

    context = {
        'title_page': _('Organizations'),
        'header_title': _('Organizations'),
        'description': _('List of Organizations'),
        'own_organizations': own_organizations,
    }

    return render(request, 'organizations/index.html', context)