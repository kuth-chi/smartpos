from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User


class PageImage(models.Model):
    alt_tag = models.CharField(max_length=100, verbose_name=_('Alt tag'))
    image = models.ImageField(upload_to='media/page/', blank=True, verbose_name=_('Image'))
    # Auto Generated
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    # Referenced models
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='page_image')
    page = models.ForeignKey('Page', on_delete=models.CASCADE, related_name='images')
    
    def __str__(self):
        return str(self.alt_tag)

class Page(models.Model):
    ORDERING_CHOICES = [
        (' ', _('Auto')),
        ('ascend', _('Ascending')), 
        ('descend', _('Descending')),
        ('order-1', _('Order 1')),
        ('order-2', _('Order 2')),
        ('order-3', _('Order 3')),
        ('order-4', _('Order 4')),
        ('order-5', _('Order 5')),
        ('order-6', _('Order 6')),
        ('order-7', _('Order 7')),
        ('order-8', _('Order 8')),
    ]
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    ordering = models.CharField(max_length=10, blank=True, default='', choices=ORDERING_CHOICES, verbose_name=_('Ordering'))
    # Auto Generated
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True)
    # Referenced models
    
    def __str__(self):
        return str(self.name)