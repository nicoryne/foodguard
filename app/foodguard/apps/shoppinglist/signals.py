from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import ShoppingList, IngredientToBuy

        
@receiver(post_save, sender=ShoppingList)
def log_shopping_list_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New shopping list created for user: {instance.user.fname} {instance.user.lname}")
    else:
        print(f"Shopping list updated for user: {instance.user.fname} {instance.user.lname}")

@receiver(pre_delete, sender=ShoppingList)
def log_shopping_list_deletion(sender, instance, **kwargs):
    print(f"Shopping list deleted for user: {instance.user.fname} {instance.user.lname}")

@receiver(post_save, sender=IngredientToBuy)
def log_ingredient_to_buy_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New ingredient added to shopping list: {instance.ingredient.name} - Quantity: {instance.quantity}")
    else:
        print(f"Ingredient updated in shopping list: {instance.ingredient.name} - Quantity: {instance.quantity}")

@receiver(pre_delete, sender=IngredientToBuy)
def log_ingredient_to_buy_deletion(sender, instance, **kwargs):
    print(f"Ingredient removed from shopping list: {instance.ingredient.name} - Quantity: {instance.quantity}")
