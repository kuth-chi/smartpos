from django.db import models
from accounts.models import User
from organizations.models import Organization
from rbac.models import Role

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    employee_id = models.CharField(max_length=20)
    date_of_joining = models.DateField()
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    
    
    