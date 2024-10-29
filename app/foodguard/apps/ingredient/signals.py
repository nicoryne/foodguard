# ingredient/signals.py
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Ingredient

@receiver(post_save, sender=Ingredient)
def log_ingredient_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New ingredient added: {instance.name}")
        
    else:
        print(f"Ingredient updated: {instance.name}")

@receiver(pre_delete, sender=Ingredient)
def log_ingredient_deletion(sender, instance, **kwargs):
    print(f"Ingredient deleted: {instance.name}")

