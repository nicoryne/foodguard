from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import User
from django.conf import settings
from ..shoppinglist.models import ShoppingList

@receiver(post_save, sender=User)
def log_user_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New user created: {instance.fname} {instance.lname} (Email: {instance.email})")
    else:
        print(f"User updated: {instance.fname} {instance.lname} (Email: {instance.email})")
        
@receiver(post_save, sender=User)
def create_shopping_list(sender, instance, created, **kwargs):
    if created:
        ShoppingList.objects.create(user=instance, capacity=10)

@receiver(pre_delete, sender=User)
def log_user_deletion(sender, instance, **kwargs):
    print(f"User deleted: {instance.fname} {instance.lname} (Email: {instance.email})")

