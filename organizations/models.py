import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
 
class Organization(models.Model):
    """
    Organization model
    """
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    local_name = models.CharField(max_length=255, blank=True, verbose_name=_("Local name"))
    slogan = models.CharField(max_length=255, blank=True, verbose_name=_("Slogan"))
    slogan_local = models.CharField(max_length=255, blank=True, verbose_name=_("Slogan local"))
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100, blank=True, verbose_name=_("Email"))
    phone = models.CharField(max_length=100, blank=True, verbose_name=_("Phone"))
    header_cover = models.ImageField(upload_to='media/organizations/cover', blank=True)
    description = models.TextField(verbose_name=_("Description"), blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    is_permanent_closed = models.BooleanField(default=False, verbose_name=_("Permanent Closed"))
    created_by = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.CASCADE) # Reference to User
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = str(uuid.uuid4())[:24].replace('-', '').lower()
        super(Organization, self).save(*args, **kwargs)
        

class OrganizationLogo(models.Model):
    """ Tracking organization logo """
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='media/organizations/logos', blank=True)
    title = models.CharField(max_length=150, blank=True)
    design_company = models.CharField(max_length=150, blank=True)
    designer_name = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.organization.name
    
    

class SocialProfile(models.Model):
    SOCIAL_CHOICES = [
        ('website', 'Website'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('instragram', 'Instagram'),
        ('x', 'X'),
        ('linkedin', 'LinkedIn'),
        ('tiktok', 'Tiktok'),
        ('discord', 'Discord'),
        ('snapchat', 'Snapchat'),
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
    ]
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, choices=SOCIAL_CHOICES, verbose_name='Social Profile')
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.name == "website":
            self.link = "https://" + self.link
        if self.name == "facebook":
            self.link = "https://www.facebook.com/" + self.link   
        if self.name == "youtube":
            self.link = "https://www.youtube.com/" + self.link
        if self.name == "linkedin":
            self.link = "https://www.linkedin.com/" + self.link
        if self.name == "tiktok":
            self.link = "https://www.tiktok.com/" + self.link
        if self.name == "discord":
            self.link = "https://discord.com/" + self.link
        if self.name == "snapchat":
            self.link = "https://www.snapchat.com/" + self.link
        if self.name == "whatsapp":
            self.link = "https://www.whatsapp.com/" + self.link
        if self.name == "telegram":
            self.link = "https://www.telegram.com/" + self.link
        super().save(*args, **kwargs)