from django.db import models
from ..users.models import User
from ..ingredient.models import Ingredient

# Classes within shopping_list/models.py
#   1. ShoppingList
#   2. IngredientsToBuy
#   3. IngredientsInCart


# Shopping List
class ShoppingList(models.Model):
    shopping_list_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shopping_list')
    capacity = models.IntegerField()
    
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
    quantity = models.IntegerField()
    in_cart = models.BooleanField(default=False)
    
    def __str__(self):
        return (
            f"Ingredient: {self.ingredient.name}\n"
            f"Quantity: {self.quantity}\n"
            f"In Cart: {'Yes' if self.in_cart else 'No'}"
        )

# Ingredients In Cart
class IngredientInCart(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredients_in_cart')
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='ingredients_in_cart')
    quantity = models.IntegerField()
    
    def __str__(self):
        return (
            f"Ingredient: {self.ingredient.name}\n"
            f"Quantity in Cart: {self.quantity}"
        )