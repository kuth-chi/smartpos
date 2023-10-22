import uuid
from django.db import models
from organizations.models import Organization
from django.utils.translation import gettext_lazy as _

# Create your models here.
   


class Business(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100, unique=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='business/logo', blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = str(uuid.uuid4())[:24].replace('-', '').lower()
        super(Business, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('Business')
        verbose_name_plural = _('Businesses')
        

class BusinessAddress(models.Model):
    business = models.OneToOneField(Business, on_delete=models.CASCADE, primary_key=True) # FK to Branche
    address = models.CharField(max_length=100, verbose_name=_('Address'))
    zipcode = models.CharField(max_length=8, verbose_name=_('Zipcode'))
    latitude = models.DecimalField(default=0.0, max_digits=9, blank=True, decimal_places=6, verbose_name=_('Latitude'))
    longitude = models.DecimalField(default=0.0, max_digits=9, blank=True, decimal_places=6, verbose_name=_('Longitude'))
    village = models.ForeignKey('addressing.Village', blank=True, null=True, on_delete=models.CASCADE)
    commune = models.ForeignKey('addressing.Commune', blank=True, null=True, on_delete=models.CASCADE)
    district = models.ForeignKey('addressing.District', blank=True, null=True, on_delete=models.CASCADE)
    province = models.ForeignKey('addressing.Province', blank=True, null=True, on_delete=models.CASCADE)
    country = models.ForeignKey('addressing.Country', blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.address + str(self.business.name)


class EstablishedDate(models.Model):
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
    name = models.CharField(max_length=100, verbose_name=_('Branch'))
    local_name = models.CharField(max_length=100, blank=True, verbose_name=_('Local name'))
    code = models.CharField(max_length=100, blank=True, verbose_name=_('Code'))
    business = models.ForeignKey(Business, on_delete=models.CASCADE) # FK for business
    grand_open = models.DateField(blank=True, null=True, verbose_name=_('Grand open'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class BranchImage(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/business/branch', blank=True)
    alt = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.alt
    
class BranchAddress(models.Model):
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE, primary_key=True) # FK to Branche
    address = models.CharField(max_length=100, verbose_name=_('Address'))
    zipcode = models.CharField(max_length=8, blank=True, null=True, verbose_name=_('Zipcode'))
    latitude = models.DecimalField(default=0.0, max_digits=9, blank=True, decimal_places=6, verbose_name=_('Latitude'))
    longitude = models.DecimalField(default=0.0, max_digits=9, blank=True, decimal_places=6, verbose_name=_('Longitude'))
    village = models.ForeignKey('addressing.Village', blank=True, null=True, on_delete=models.CASCADE)
    commune = models.ForeignKey('addressing.Commune', blank=True, null=True, on_delete=models.CASCADE)
    district = models.ForeignKey('addressing.District', blank=True, null=True, on_delete=models.CASCADE)
    province = models.ForeignKey('addressing.Province', blank=True, null=True, on_delete=models.CASCADE)
    country = models.ForeignKey('addressing.Country', blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.address
    
    
        