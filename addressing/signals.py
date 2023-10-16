import logging
from django.db.models.signals import pre_delete
from django.core.files.storage import default_storage
from django.dispatch import receiver
from addressing.models import Country

logger = logging.getLogger(__name__)

@receiver(pre_delete, sender=Country)
def delete_country_flag(send, instance, **kwargs):
    if instance.flag:
        try:
            # Delete the file from storage
            default_storage.delete(instance.flag.path)
        except Exception as e:
            # Handle exceptions here, for example, log the error
            # You can customize this based on your error handling needs
            logger.error(f"Failed to delete flag image: {e}")
            