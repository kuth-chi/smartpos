from django.db import models
from accounts.models import User
from django.contrib.auth.models import Permission


# ORG PERMISSION
class Organization:
    """
        Create Organization permissions
    """
    FULL_ACCESS = 'organization_full_access'

Permission.objects.create(
    codename=Organization.FULL_ACCESS, 
    name='Organization Full Access (Create, Edit, Delete)'
)
    


# Create your models here.
class Role(models.Model):
    """ Role model define to assign to Employee"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    permissions = models.ManyToManyField(Permission)
    updated_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)
