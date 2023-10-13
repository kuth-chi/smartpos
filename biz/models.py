from django.db import models
from organizations.models import Organization
from django.utils.translation import gettext_lazy as _

# Create your models here.
   


class Business(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='business/logo', blank=True)
    description = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Business')
        verbose_name_plural = _('Businesses')


class EstimatedDate(models.Model):
    """
    Estimated Date of Business
    """
    year = models.IntegerField(verbose_name='Year')
    month = models.IntegerField(verbose_name='Month')
    day = models.IntegerField(verbose_name='Day')
    hour = models.IntegerField(verbose_name='Hour')
    minute = models.IntegerField(verbose_name='Minute')
    second = models.IntegerField(verbose_name='Second')
    business = models.OneToOneField(Business, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.year
        
        
class Branch(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, blank=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE) # FK for business
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class BranchAddress(models.Model):
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE, primary_key=True) # FK to Branche
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.address
    
    
        