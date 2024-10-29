from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'apps.users'
    
    def ready(self):
        from apps.users import signals
