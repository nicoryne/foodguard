from django.apps import AppConfig

class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'apps.notifications'
    
    def ready(self):
        from apps.notifications import signals
