from django.db import models
from django.utils import timezone

from apps.ingredient.models import Ingredient
from ..users.models import User

# Classes within inventory/models.py
#   1. Inventory
#   2. InventoryIngredientOwnership

# Inventory
class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    ingredient_quantity = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='inventory')
    
    def __str__(self):
        return (
            f"Inventory ID: {self.inventory_id}\n"
            f"User: {self.user.fname} {self.user.lname}\n"
            f"Ingredient Quantity: {self.ingredient_quantity}\n"
            f"Last Updated: {self.updated_at}"
        )
    
    
# Inventory-Ingredient Ownership
class InventoryIngredientOwnership(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='inventory_ingredient_ownership')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='inventory_ingredient_ownership')
    purchase_date = models.DateField()
    expiry_date = models.DateField()
    quantity = models.IntegerField()
    
    @property
    def freshness(self):
        today = timezone.now().date()
        total_shelf_life = (self.expiry_date - self.purchase_date).days
        remaining_shelf_life = (self.expiry_date - today).days
        
        if remaining_shelf_life < 0:
            return 0.0

        return round(remaining_shelf_life / total_shelf_life, 4) if total_shelf_life > 0 else 0.0
    
    def __str__(self):
        return (
            f"Ingredient: {self.ingredient.name}\n"
            f"Quantity: {self.quantity}\n"
            f"Purchase Date: {self.purchase_date}\n"
            f"Expiry Date: {self.expiry_date}\n"
            f"Freshness: {self.freshness:.4f}"
        )