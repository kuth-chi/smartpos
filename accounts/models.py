import random, string, uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _
from .managers import UserAccountManager
from addressing.models import Country, Province, District, Commune, Village


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    """
        Abstract user table for addtional information
    """
    GENDER_CHOICE = [
        ("F", _("Female")),
        ("M", _("Male")),
        ("O", _("Other")),
    ]
    uuid = models.UUIDField(_('uuid'), unique=True,
                            default=uuid.uuid4, editable=False)
    username = models.CharField(
        _('username'), unique=True, max_length=35, blank=True)
    email = models.EmailField(_('email'), max_length=25, blank=True)
    website = models.URLField(blank=True, null=True, verbose_name=_('Website'))
    avatar = models.ImageField(
        upload_to="media/user/images/avatar/", blank=True, verbose_name=_("Avatar")
    )
    primary_phone = models.CharField(
        max_length=16, blank=True, verbose_name=_('Primary phone'))
    local_name = models.CharField(max_length=50, blank=True, verbose_name=_(
        'Local name'), help_text=_("The name in your language"))
    first_name = models.CharField(
        max_length=50, blank=True, verbose_name=_('First name'))
    last_name = models.CharField(
        max_length=50, blank=True, verbose_name=_('Last name'))
    dob = models.DateField(null=True, blank=True,
                           verbose_name=_('Date of Birth'))
    biography = models.CharField(
        max_length=150, blank=True, null=True, help_text=_('Describe your self'))
    recovery_email = models.EmailField(
        null=True, blank=True, verbose_name='Recover Email')
    gender = models.CharField(
        max_length=10, default="O", choices=GENDER_CHOICE, verbose_name=_('Gender'))
    last_login = models.DateTimeField(auto_now=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False, verbose_name=_('Public'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Staff'))
    is_superuser = models.BooleanField(default=False, verbose_name=_('Superuser'))
    updated_date = models.DateTimeField(verbose_name=_('update at'), auto_now=True)
    created_date = models.DateTimeField(verbose_name=_('submitted at'), auto_now_add=True)

    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = []
    unique_together = ("username", "email", "primary_phone")
    objects = UserAccountManager()

    # Add related_name for groups
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='user_set'  # Use a meaningful related_name
    )
    
    # Add related_name for user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='user_set_permissions'  # Use a meaningful related_name
    )

    class Meta:
        unique_together = ['username', 'email', 'primary_phone']
        


    # Generate Username when signup
    def save(self, *args, **kwargs):
        if not self.username:
            # Generate a random 8-character string for the username
                
            
            if self.first_name and self.last_name:
                generate_username = "".join(random.choices(string.ascii_letters + string.digits, k=8))
                self.username = (str(self.first_name + self.last_name + generate_username)).lower()
                
            else:
                self.username = ("".join(random.choices(string.ascii_letters + string.digits, k=16))).lower()
                
        super().save(*args, **kwargs)
    def clean(self):
        # Ensure at lease one of username, email or primary_phone is provided.
        if not any([self.username, self.email, self.primary_phone]):
            raise ValidationError(
                _("Please fill in at least one of the fields."))

        # Check for duplicate values in username, email or primary_phone is filled
        if self.username and User.objects.exclude(pk=self.pk).filter(username=self.username).exists():
            raise ValidationError(
                _("A user with this username already exists. Please choose another username."))
        if self.email and User.objects.exclude(pk=self.pk).filter(email=self.email).exists():
            raise ValidationError(
                _("A user with this email already exists. Please choose another email."))
        if self.primary_phone and User.objects.exclude(pk=self.pk).filter(primary_phone=self.primary_phone).exists():
            raise ValidationError(
                _("A user with this phone number already exists. Please choose another phone number."))
        super().clean()

    def __str__(self):
        if self.username:
            return self.username
        elif self.email:
            return self.email
        elif self.primary_phone:
            return self.primary_phone

# Alternative Phone
class AlternativePhone(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='alternative_phone',
        blank=True,
        null=True
    )
    type = models.CharField(max_length=20, blank=True, unique=True, default="mobile", choices=[
        ('mobile', _('Mobile')),
        ('home', _('Home')),
        ('work', _('Work')),
        ('other', _('Other')),
    ], verbose_name=_('Type'))
    number = models.PositiveIntegerField(blank=True, unique=True, verbose_name=_('Number'))
    updated_date = models.DateTimeField(_('update at'), auto_now=True)
    created_date = models.DateTimeField(_('submitted at'), auto_now_add=True)
    
    def __str__(self):
        return str(self.number)

class VerificationAccount(models.Model):
    VERIFICATION_TYPE_CHOICE = [
        ('passport', _('Passport')),
        ('id', _('National Identity')),
        ('other', _('Other Identity')),
    ]

    STATUS_CHOICE = [
        ('reviewing', _('Reviewing')),
        ('rejected', _('Rejected')),
        ('verified', _('Verified')),
    ]

    type = models.CharField(_("type"), max_length=150, default="passport", choices=VERIFICATION_TYPE_CHOICE)
    first_name = models.CharField(_("first_name"), max_length=50)
    last_name = models.CharField(_("last_name"), max_length=50)
    dob = models.DateField(_('date of birth'), blank=True)
    social_reference = models.TextField(_("social_reference"), max_length=500, blank=True, help_text=_(
        "provide link of your profiles for more reference information"))
    status = models.CharField(
        _("status"), max_length=10, default="reviewing", choices=STATUS_CHOICE)
    updated_date = models.DateTimeField(_('update at'), auto_now=True)
    created_date = models.DateTimeField(_('submitted at'), auto_now_add=True)
 

    def __str__(self):
        if self.type:
            return self.type
        elif self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        else:
            return self.pk


class AccountGallery(models.Model):
    """
    Make user uploaded into account gallery
    """
    
    def __init__(self, *args, **kwargs):
        super(AccountGallery, self).__init__(*args, **kwargs)
        self.is_cover_set = False
        
    uuid = models.UUIDField(verbose_name=_(
        "UUID"), default=uuid.uuid4, editable=False, unique=True)
    is_avatar = models.BooleanField(
        default=False, unique=True, verbose_name=_('Is Avatar'))
    is_cover_set = models.BooleanField(default=False, verbose_name=_('Is cover'))
    alt_image = models.CharField(
        max_length=150, blank=True, verbose_name=_('alternative image image'))
    image = models.ImageField(
        upload_to="media/user/images/account/", blank=True, verbose_name=_("image"))
    uploaded_on = models.DateTimeField(
        auto_now_add=True, verbose_name="Uploaded Date")
    uploaded_by = models.ForeignKey(
        User, related_name="user_gallery", blank=True, null=True, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(_('update at'), auto_now=True)
    created_date = models.DateTimeField(_('submitted at'), auto_now_add=True)
    
    
    # Fix with import Manager
    objects = models.Manager()
    def __str__(self):
        if self.alt_image:
            return str(self.alt_image)
        elif self.uploaded_on:
            return str(self.uploaded_on)
        else:
            return str(self.uuid)

    class Meta:
        verbose_name = 'AccountGallery'
        verbose_name_plural = 'AccountGalleries'


    def set_profile(self):
        existing_user_profile = AccountGallery.objects.filter(
            uploaded_by=self.uploaded_by, is_avatar=True).first()
        if existing_user_profile:
            existing_user_profile.is_avatar = False
            existing_user_profile.save()

        self.is_avatar = True
        self.save()

    def set_covered_image(self):
        existing_user_cover = AccountGallery.objects.filter(
            uploaded_by=self.uploaded_by, is_cover_set=True).count()
        if existing_user_cover >= 7:
            raise ValidationError("Maximum set images allowed is hit")
        self.is_cover_set = True
        self.save()


class SettingUser(models.Model):
    """
    Record user settings here
    """
    THEME_MODE_CHOICES = (
        ('dark', _('Dark Mode')),
        ('light', _('Light Mode')),
        ('auto', _('System Mode')),
    )
    
    # Rename 'user_id' to 'user' for clarity
    user = models.OneToOneField(User, related_name="accounts_UserSettings", null=True, on_delete=models.CASCADE)
    
    is_first_name = models.BooleanField(default=True)
    timezone = models.CharField(
        max_length=25, blank=True, verbose_name=_('Timezone'))
    language = models.CharField(
        max_length=25, default='en', verbose_name=_('Language'), choices=(
            ('en', _('English')),
            ('km', _('Khmer')),
        ))
    date_format = models.CharField(
        max_length=25, default='%d-%m-%Y', blank=True, verbose_name=_('Date Format'),
        choices=(
            ('%d-%m-%Y', _('DD-MM-YYYY')),
            ('%d-%m-%y', _('DD-MM-YY')),
            ('%a, %d %b %Y', _('Mon, DD MMM YYYY')),
            ('%A, %d %B %Y', _('Mon, DD MMM YYYY')),
            ('%B %d, %Y', _('January DD, YYYY')),
            ('%m-%d-%y', _('MM-DD-YY')),
            ('%m-%d-%Y', _('MM-DD-YYYY')),
            ('%y-%m-%d', _('YY-MM-DD')),
            ('%Y-%m-%d', _('YYYY-MM-DD')),
        ))
    
    updated_date = models.DateTimeField(_('update at'), auto_now=True)
    created_date = models.DateTimeField(_('submitted at'), auto_now_add=True)
    theme = models.CharField(max_length=12, default='auto', verbose_name=_('Theme Mode'), choices=THEME_MODE_CHOICES)

    def __str__(self):
        return str(self.user)+'\'s Settings'


class ActiveDevice(models.Model):
    """
    Represents an active device.
    
    This class stores information about a device that is currently active.
    It contains fields such as the device's name, operating system, browser,
    IP address, and latitude.
    """
    name = models.CharField(max_length=100, blank=True,
                            verbose_name=_('Device\'s Name'))
    os = models.CharField(max_length=100, blank=True,
                          verbose_name=_('Device\'s OS'))
    browser = models.CharField(
        max_length=100, blank=True, verbose_name=_('Browser'))
    ip_address = models.CharField(
        max_length=250, blank=True, verbose_name="Device\'s IP Address")
    lat = models.CharField(max_length=10, blank=True,
                           verbose_name=_('Latitude'))
    log = models.CharField(max_length=10, blank=True,
                           verbose_name=_('Longitude'))
    last_login_time = models.DateTimeField(auto_now=True, verbose_name=_('Last Login Time'))
    login_time = models.DateTimeField(auto_now_add=True, verbose_name=_('Login Time'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))
    access_token = models.CharField(max_length=255, blank=True, verbose_name=_('Access Token'))
    user = models.ForeignKey(User, related_name="active_device", blank=True, null=True, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(_('update at'), auto_now=True)
    created_date = models.DateTimeField(_('submitted at'), auto_now_add=True)
    	

    def __str__(self):
        if self.name:
            return self.name
        elif self.os:
            return self.os
        else:
            return self.ip_address
        
class Location(models.Model):
    latitude = models.FloatField(default=0.0, verbose_name=_('Latitude'))
    longitude = models.FloatField(default=0.0, verbose_name=_('Longitude'))
    updated_date = models.DateTimeField(_('update at'), auto_now=True)
    created_date = models.DateTimeField(_('submitted at'), auto_now_add=True)
    
    def __str__(self):
        return str(self.latitude) + ", " + str(self.longitude)
        
class UserAddress(models.Model):
    ADDRESS_CHOICES = (
        ('home', _('Home')),
        ('work', _('Work')),  
    )
    name = models.CharField(max_length=250, blank=True, default=ADDRESS_CHOICES[0], choices=ADDRESS_CHOICES, verbose_name=_('Name'))
    user = models.ForeignKey(User, related_name="user_address", on_delete=models.CASCADE)
    address = models.CharField(max_length=250, blank=True, verbose_name=_('Address'))
    village = models.ForeignKey(Village, related_name="address_village", null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('Village'))
    commune = models.ForeignKey(Commune, related_name="address_commune", null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('Commune'))
    city = models.ForeignKey(District, related_name="address_city", null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('City'))
    state = models.ForeignKey(Province, related_name="address_province", null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('State'))
    country = models.ForeignKey(Country, related_name="address_country", null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('Country'))
    zip = models.PositiveBigIntegerField(blank=True, verbose_name=_('Zip'))
    location = models.ForeignKey(Location, related_name="address_location", null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('Location'))
    updated_date = models.DateTimeField(_('update at'), auto_now=True)
    created_date = models.DateTimeField(_('submitted at'), auto_now_add=True)
    
    def __str__(self):
        if self.user:
            return f"{self.user}\'s {self.address},{self.state}, {self.country}, {self.zip}"

    
    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
    

class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField() # Regular expression pattern to validate URLs
    custom_logo = models.ImageField(upload_to='media/social_media_logos/', blank=True, null=True)
    updated_date = models.DateTimeField(_('update at'), auto_now=True)
    created_date = models.DateTimeField(_('submitted at'), auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class UserSocial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)  # User's username or profile link
    updated_date = models.DateTimeField(_('update at'), auto_now=True)
    created_date = models.DateTimeField(_('submitted at'), auto_now_add=True)
    
    def __str__(self):
        return self.username