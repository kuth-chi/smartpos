from django.apps import AppConfig


class AddressingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "addressing"
    
    def ready(self):
        import addressing.signals