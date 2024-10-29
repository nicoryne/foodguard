from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Inventory, InventoryIngredientOwnership
from apps.notifications.models import Notification

@receiver(post_save, sender=Inventory)
def log_inventory_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New inventory created for user: {instance.user.fname} {instance.user.lname}")
        
        Notification.objects.create(
            user=instance.user,
            title="Inventory Created",
            description=f"Your inventory has been created with ID: {instance.inventory_id}."
        )
    else:
        print(f"Inventory updated for user: {instance.user.fname} {instance.user.lname}")

@receiver(pre_delete, sender=Inventory)
def log_inventory_deletion(sender, instance, **kwargs):
    print(f"Inventory deleted for user: {instance.user.fname} {instance.user.lname}")
    
    Notification.objects.create(
        user=instance.user,
        title="Inventory Deleted",
        description=f"Your inventory with ID: {instance.inventory_id} has been deleted."
    )

@receiver(post_save, sender=InventoryIngredientOwnership)
def log_inventory_ingredient_ownership_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New ownership record created for ingredient: {instance.ingredient.name}")
        
        Notification.objects.create(
            user=instance.inventory.user,
            title="Ingredient Added to Inventory",
            description=f"{instance.quantity} of {instance.ingredient.name} has been added to your inventory."
        )
    else:
        print(f"Ownership record updated for ingredient: {instance.ingredient.name}")

@receiver(pre_delete, sender=InventoryIngredientOwnership)
def log_inventory_ingredient_ownership_deletion(sender, instance, **kwargs):
    print(f"Ownership record deleted for ingredient: {instance.ingredient.name}")
    
    Notification.objects.create(
        user=instance.inventory.user,
        title="Ingredient Removed from Inventory",
        description=f"{instance.quantity} of {instance.ingredient.name} has been removed from your inventory."
    )
