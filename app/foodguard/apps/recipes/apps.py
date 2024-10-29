from django.apps import AppConfig

class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'apps.recipes'

    def ready(self):
        from apps.recipes import signals