from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from ..shoppinglist.models import ShoppingList
from ..inventory.models import Inventory
from .models import Profile 

@receiver(post_save, sender=User)
def log_user_created(sender, instance, created, **kwargs):
    if created:
        print(f"New user created: {instance.username} (Email: {instance.email})")
    else:
        print(f"User updated: {instance.username}")
        


        
        
        

        
        
        
        
