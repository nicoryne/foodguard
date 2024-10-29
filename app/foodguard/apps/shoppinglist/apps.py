from django.apps import AppConfig

class ShoppingListConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'apps.shoppinglist'
    
    def ready(self):
        from apps.shoppinglist import signals
