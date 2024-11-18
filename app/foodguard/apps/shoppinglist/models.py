from django.db import models
from ..users.models import User
from ..ingredient.models import Ingredient

# Shopping List
class ShoppingList(models.Model):
    shopping_list_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shopping_list')
    
    @property
    def capacity(self):
        # Count the number of associated IngredientToBuy objects
        return self.ingredients_to_buy.count()
    
    def clear_ingredients(self):
        # Delete all associated IngredientToBuy objects
        self.ingredients_to_buy.all().delete()
    
    def __str__(self):
        # String representation of the Shopping List
        return (
            f"Shopping List ID: {self.shopping_list_id}\n"
            f"User: {self.user.fname} {self.user.lname}\n"
            f"Capacity: {self.capacity}"
        )

# Ingredient To Buy
class IngredientToBuy(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredients_to_buy')
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='ingredients_to_buy')
    quantity = models.PositiveIntegerField()  # Ensure only positive integers for quantity
    in_cart = models.BooleanField(default=False)
    
    def toggle_in_cart(self):
        # Toggle the in_cart status and save the instance
        self.in_cart = not self.in_cart
        self.save()
    
    def __str__(self):
        # String representation of the IngredientToBuy
        return (
            f"Ingredient: {self.ingredient.name}\n"
            f"Quantity: {self.quantity}\n"
            f"In Cart: {'Yes' if self.in_cart else 'No'}"
        )
