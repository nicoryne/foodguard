from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Notification

@receiver(post_save, sender=Notification)
def log_notification_creation(sender, instance, created, **kwargs):
    if created:
        print(f"Notification created for user: {instance.user.username}")
       
       
@receiver(pre_delete, sender=Notification)
def log_notification_deletion(sender, instance, **kwargs):
    print(f"Notification deleted for user: {instance.user.username} with title: {instance.title}")
