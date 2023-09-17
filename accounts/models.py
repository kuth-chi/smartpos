import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _
from .managers import UserAccountManager


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
    uuid = models.UUIDField(_('uuid'), unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_('username'), unique=True, max_length=35, blank=True)
    email = models.EmailField(_('email'), max_length=25, blank=True)
    primary_phone = models.CharField(max_length=12, blank=True, verbose_name=_('Primary phone'))
    local_name = models.CharField(max_length=50, blank=True, verbose_name=_('Local name'), help_text=_("The name in your language"))
    first_name = models.CharField(max_length=50, blank=True, verbose_name=_('First name'))
    last_name = models.CharField(max_length=50, blank=True, verbose_name=_('Last name'))
    dob = models.DateField(null=True, blank=True, verbose_name=_('Date of Birth'))
    biography = models.CharField(max_length=150, blank=True, null=True, help_text=_('Describe your self'))
    recovery_email = models.EmailField(null=True, blank=True, verbose_name='Recover Email')
    gender = models.CharField(max_length=10, default="Other", choices=GENDER_CHOICE, verbose_name=_('Gender'))
    last_login = models.DateTimeField(auto_now=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    objects = UserAccountManager()
    
    # Add related_name for groups
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_set'  # Change this to a unique name
    )
    
    # Add related_name for user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set_permissions'  # Change this to a unique name
    )

    class Meta:
        unique_together = ['username', 'email', 'primary_phone']

    def __str__(self):
        if self.username:
            return self.username
        elif self.email:
            return self.email
        elif self.primary_phone:
            return self.primary_phone
        



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

    user = models.ForeignKey(User, related_name='verification_account', blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(_("type"), max_length=150, default="passport", choices=VERIFICATION_TYPE_CHOICE)
    first_name = models.CharField(_("first_name"), max_length=50)
    last_name = models.CharField(_("last_name"), max_length=50)
    dob = models.DateField(_('date of birth'))
    social_reference = models.TextField(_("social_reference"), max_length=500, blank=True, help_text=_("provide link of your profiles for more reference information"))
    status = models.CharField(_("status"), max_length=10, default="reviewing", choices=STATUS_CHOICE)
    created_date = models.DateTimeField(_('submitted at'), auto_now_add=True)
    updated_date = models.DateTimeField(_('update at'), auto_now=True)

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
    uuid = models.UUIDField(verbose_name=_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    is_avatar = models.BooleanField(default=False, unique=True, verbose_name=_('Is Avatar'))
    is_cover = models.BooleanField(default=False, verbose_name=_('Is cover'))
    alt_image = models.CharField(max_length=150, blank=True, verbose_name=_('alternative image image'))
    image = models.ImageField(upload_to="user/images/account/", blank=True, verbose_name=_("image"))
    uploaded_on = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded Date")
    uploaded_by = models.ForeignKey(User, related_name="user_gallery", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.alt_image:
            return self.alt_image
        elif self.uploaded_on:
            return self.uploaded_on
        else:
            return self.uuid
        
    class Meta:
        verbose_name = 'AccountGallery'
        verbose_name_plural = 'AccountGalleries'

    def set_profile(self):
        existing_user_profile = AccountGallery.objects.filter(uploaded_by=self.uploaded_by, is_avatar=True).first()
        if existing_user_profile:
            existing_user_profile.is_avatar = False
            existing_user_profile.save()

        self.is_avatar = True
        self.save()

    def set_covered_image(self):
        existing_user_cover = AccountGallery.objects.filter(uploaded_by=self.uploaded_by, is_cover=True).count()
        if existing_user_cover >= 7:
            raise ValidationError("Maximum set images allowed is hit")
        self.is_cover = True
        self.save()

    


class SettingUser(models.Model):
    """
        Record user settings here
    """
    user = models.ForeignKey(User, related_name="UserSettings", null=True, blank=True, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=25, blank=True, verbose_name=_('Timezone'))
    language = models.CharField(max_length=25, blank=True, verbose_name=_('Language'))
    timestamp = models.DateTimeField(auto_now_add=True)
    is_dark = models.BooleanField(default=False, verbose_name=_('Dark Mode'))

    def __str__(self):
        if self.user:
            return self.user
        else:
            return self.pk
        


class ActiveDevice(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name=_('Device\'s Name'))
    os = models.CharField(max_length=100, blank=True, verbose_name=_('Device\'s OS'))
    browser = models.CharField(max_length=100, blank=True, verbose_name=_('Browser'))
    ip_address = models.CharField(max_length=250, blank=True, verbose_name="Device\'s IP Address")
    lat = models.CharField(max_length=10, blank=True, verbose_name=_('Latitude'))
    log = models.CharField(max_length=10, blank=True, verbose_name=_('Longitude'))
    last_login_time = models.DateTimeField(auto_now=True, verbose_name=_('Last Login Time'))
    login_time = models.DateTimeField(auto_now_add=True, verbose_name=_('Login Time'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))
    access_token = models.CharField(max_length=255, blank=True, verbose_name=_('Access Token'))
    user = models.ForeignKey(User, related_name="active_device", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.name:
            return self.name
        elif self.os:
            return self.os
        else:
            return self.ip_address