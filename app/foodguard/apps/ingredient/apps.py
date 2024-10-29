from django.apps import AppConfig

class IngredientConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'apps.ingredient'
    
    def ready(self):
        from apps.ingredient import signals


