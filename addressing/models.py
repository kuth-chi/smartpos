import logging
from django.db import models
from django.core.files.storage import default_storage
from django.utils.translation import gettext_lazy as _

    
# FOR COUNTRY DATABASE
class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name=_('Country'))
    name_local = models.CharField(max_length=100, blank=True, verbose_name=_('Local name'))
    flag = models.ImageField(upload_to="media/country/images/flag/", blank=True, verbose_name=_('Flag'))
    short_name = models.CharField(max_length=3, blank=True, verbose_name=_('Short name'))
    code = models.IntegerField(blank=True, default=0, verbose_name=_('Code'))
    currency = models.CharField(max_length=3, blank=True, verbose_name=_('Currency'))
    primary_language = models.CharField(max_length=50, blank=True, verbose_name=_('Primary language'))
    alt_languages = models.CharField(max_length=250, blank=True, verbose_name=_('Alternative languages'))
    border_with = models.CharField(max_length=250, blank=True, default='', verbose_name=_('Border with'))
    border_length = models.IntegerField(blank=True, default=0, verbose_name=_('Border length'))
    landmark = models.IntegerField(blank=True, default=0, verbose_name=_('Landmark'))
    is_before_chris = models.BooleanField(default=False, blank=True)
    is_public = models.BooleanField(default=False, blank=True, verbose_name=_('Public'))
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = _('Countries')

    def __str__(self):
        return f'{self.name}'
    
    def delete(self, *args, **kwargs):
        flag_path = self.flag.path
        super().delete(*args, **kwargs)
        
        logger = logging.getLogger(__name__)
        # Delete image from storage
        if flag_path and self.__class__.objects.filter(flag=flag_path).count() == 0:
            try:
                # Delete the file from storage
                default_storage.delete(flag_path)
            except Exception as e:
                    # Handle exceptions here, for example, log the error
                    # You can customize this based on your error handling needs
                    logger.error(f"Failed to delete flag image: {e}")


class Province(models.Model):
    TYPE_CHOICES = (
        ('province', _('Province')),
        ('capital', _('Capital')),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='province', verbose_name=_('Type'))
    country_id = models.ForeignKey(Country, related_name='province', on_delete=models.CASCADE, blank=True, null=True, default=False)
    name = models.CharField(max_length=100, blank=True, verbose_name=_('name'))
    name_local = models.CharField(max_length=100, blank=True, verbose_name=_('Local name'))
    short_name = models.CharField(max_length=3, blank=True, verbose_name=_('Short name'))
    code = models.IntegerField(blank=True, verbose_name=_('Code'))
    border_with = models.CharField(max_length=250, blank=True, verbose_name=_('Border with'))
    border_length = models.IntegerField(blank=True, verbose_name=_('Border length'))
    leader = models.CharField(max_length=3, blank=True, verbose_name=_('Leader'))
    hotline = models.IntegerField(verbose_name=_('Hotline'))
    is_public = models.BooleanField(default=False, blank=True, verbose_name=_('Public'))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class District(models.Model):
    TYPE_CHOICES = (
        ('district', _('District')),
        ('khan', _('Khan')),
        ('city', _('City')),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='district')
    province_id = models.ForeignKey(Province, related_name='district', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, verbose_name=_('name'))
    name_local = models.CharField(max_length=100, blank=True, verbose_name=_('Local name'))
    short_name = models.CharField(max_length=3, blank=True, verbose_name=_('Short name'))
    code = models.IntegerField(blank=True, verbose_name=_('Code'))
    border_with = models.CharField(max_length=250, blank=True, verbose_name=_('Border with'))
    border_length = models.IntegerField(blank=True, verbose_name=_('Border length'))
    hotline = models.IntegerField(blank=True, verbose_name=_('Hotline'))
    is_public = models.BooleanField(default=False, blank=True, verbose_name=_('Public'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('timestamp'))

    def __str__(self):
        return self.name


class Commune(models.Model):
    TYPE_CHOICES = (
        ('commune', _('Commune')),
        ('sangkat', _('Sangkat')),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='commune')
    district_id = models.ForeignKey(District, related_name='commune', on_delete=models.CASCADE, null=True, blank=True, default=False)
    name = models.CharField(max_length=100, blank=True, verbose_name=_('name'))
    name_local = models.CharField(max_length=100, blank=True, verbose_name=_('Local name'))
    short_name = models.CharField(max_length=3, blank=True, verbose_name=_('Short name'))
    code = models.IntegerField(blank=True, verbose_name=_('Code'))
    border_with = models.CharField(max_length=250, blank=True, verbose_name=_('Border with'))
    border_length = models.IntegerField(blank=True, verbose_name=_('Border length'))
    hotline = models.IntegerField(blank=True, verbose_name=_('Hotline'))
    is_public = models.BooleanField(default=False, blank=True, verbose_name=_('Public'))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Village(models.Model):
    commune_id = models.ForeignKey(Commune, on_delete=models.CASCADE, blank=True, null=True)  # Refer to Commune ID
    name = models.CharField(max_length=100, blank=True, verbose_name=_('name'))
    name_local = models.CharField(max_length=100, blank=True, verbose_name=_('Local name'))
    short_name = models.CharField(max_length=3, blank=True, verbose_name=_('Short name'))
    code = models.IntegerField(blank=True, verbose_name=_('Code'))
    border_with = models.CharField(max_length=250, default=False, blank=True, verbose_name=_('Border with'))
    border_length = models.IntegerField(blank=True, verbose_name=_('Border length'))
    hotline = models.IntegerField(blank=True, verbose_name=_('Hotline'))
    is_public = models.BooleanField(default=False, blank=True, verbose_name=_('Public'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('Timestamp'))

    def __str__(self):
        return self.name
    
# Create your models here.
class CountryLeader(models.Model):
    LEADER_POSITION_CHOICES = (
        ('prime_minister', _('Prime Minister')),
        ('president', _('President')),
    )
    first_name = models.CharField(max_length=100, blank=True, verbose_name=_('Fist name'))
    last_name = models.CharField(max_length=100, blank=True, verbose_name=_('Last name'))
    local_name = models.CharField(max_length=100, blank=True, verbose_name=_('Local name'))
    gender = models.CharField(max_length=100, blank=True, verbose_name=_('Gender'))
    born = models.DateField(blank=True, verbose_name=_('Born'))
    position = models.CharField(max_length=100, default='prime_minister', blank=True, choices=LEADER_POSITION_CHOICES, verbose_name=_('Position'))
    start_on = models.DateField(blank=True, verbose_name=_('Start on'))
    exit_on = models.DateField(blank=True, verbose_name=_('Exit on'))
    contributor = models.CharField(max_length=100, blank=True, verbose_name=_('Contributor'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    country_id = models.ForeignKey(Country, related_name='country_leader', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name