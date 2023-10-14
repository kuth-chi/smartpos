from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User

class PlanFeature(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

# Create your models here.
class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    badge = models.ImageField(upload_to='media/badges/', verbose_name=_('Badge'))
    description = models.TextField(verbose_name=_('Description'))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(verbose_name=_('Duration'))  # Subscription duration in days
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.name
    

class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=True, verbose_name=_('Start Date'))
    end_date = models.DateTimeField(verbose_name=_('End Date'))
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def save(self, *args, **kwargs):
        # Calculate the end date based on the plan's duration
        self.end_date = self.start_date + timezone.timedelta(days=self.plan.duration)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.plan.name}'
