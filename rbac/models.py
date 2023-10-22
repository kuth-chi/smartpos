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
    
class OrganizationEmployee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organization_employee')
    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True)
    joining_date = models.DateField(blank=True, null=True, verbose_name="Joining Date")
    exit_date = models.DateField(null=True, blank=True, verbose_name="Leaving Date")
    status = models.CharField(max_length=20, default="active", choices=[("active", "active"), ("suspended", "suspended"), ("terminated", "terminated")])  # Status choices: "active," "suspended," "terminated"
    email = models.EmailField(blank=True, verbose_name="Email")
    phone = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to="media/employees/profile_pictures", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.organization}"

# Create your models here.
class Role(models.Model):
    """ Role model define to assign to Employee"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    permissions = models.ManyToManyField(Permission)
    updated_add = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.CASCADE)
    updated_by = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)
