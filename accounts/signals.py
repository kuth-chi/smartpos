import os
import logging
from .models import SettingUser, User, SocialMedia
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_setting_user(sender, instance, created, **kwargs):
    if created:
        SettingUser.objects.create(user=instance)
        
        
        
logger = logging.getLogger(__name__)
@receiver(pre_delete, sender=User)
def delete_user_avatar(sender, instance, **kwargs):
    # Check if the instance has a custom avatar and if it exists in storage
    if instance.avatar and instance.avatar.path:
        try:
            # Delete the file from storage
            os.remove(instance.avatar.path)
        except Exception as e:
            # Handle any exceptions that may occur during deletion
            logger.error(f"Error deleting image: {e}")
        
      
@receiver(pre_delete, sender=SocialMedia)
def delete_social_media_image(sender, instance, **kwargs):
    # Check if the instance has a custom logo and if it exists in storage
    if instance.custom_logo and instance.custom_logo.path:
        try:
            # Delete the file from storage
            os.remove(instance.custom_logo.path)
        except Exception as e:
            # Handle any exceptions that may occur during deletion
            logger.error(f"Error deleting image: {e}")
