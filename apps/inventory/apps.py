from django.apps import AppConfig

class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'apps.inventory'
    
    def ready(self):
        from apps.inventory import signals


