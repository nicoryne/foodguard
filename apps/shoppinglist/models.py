from django.db import models
from ..users.models import User
from ..ingredient.models import Ingredient

# Shopping List
class ShoppingList(models.Model):
    shopping_list_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shopping_list')
    
    @property
    def capacity(self):
        return self.ingredients_to_buy.count()
    
    def clear_ingredients(self):
        self.ingredients_to_buy.all().delete()
    
    def __str__(self):
        return (
            f"Shopping List ID: {self.shopping_list_id}\n"
            f"User: {self.user.fname} {self.user.lname}\n"
            f"Capacity: {self.capacity}"
        )

# Ingredient To Buy
class IngredientToBuy(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredients_to_buy')
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='ingredients_to_buy')
    quantity = models.PositiveIntegerField() 
    in_cart = models.BooleanField(default=False)
    
    def toggle_in_cart(self):
        self.in_cart = not self.in_cart
        self.save()
    
    def __str__(self):
        return (
            f"Ingredient: {self.ingredient.name}\n"
            f"Quantity: {self.quantity}\n"
            f"In Cart: {'Yes' if self.in_cart else 'No'}"
        )
