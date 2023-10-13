from django.shortcuts import render
from organizations.models import Organization


def org_dashboard_view(request, uuid, **kwargs):
    uuid = Organization.objects.get(uuid=uuid)
    
    context = {
        'title_page': _('Dashboard'),
        'header_title': _('Dashboard'),
    }
    return render(request, 'org/pages/dashboard.html', context)