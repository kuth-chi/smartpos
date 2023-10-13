from django.contrib import admin
from .models import Organization, SocialProfile, OrganizationLogo

# Register your models here.

admin.site.register(Organization)
admin.site.register(SocialProfile)
admin.site.register(OrganizationLogo)
