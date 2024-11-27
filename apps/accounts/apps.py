from django.apps import AppConfig

class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'apps.accounts'
    
    def ready(self):
        from apps.accounts import signals
