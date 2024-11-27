from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from apps.ingredient.models import Ingredient


# Classes within inventory/models.py
#   1. Inventory
#   2. InventoryIngredientOwnership

# Inventory
class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    ingredient_quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='inventory')
    
    
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