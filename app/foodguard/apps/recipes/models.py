from django.db import models
from ..users.models import User
from ..inventory.models import Ingredient

# Classes within recipes/models.py
#   1. Recipe
#   2. RecipeIngredients
#   3. RecipeUserSaved
#   4. RecipeUserRating


# Recipe
class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=35)
    duration = models.CharField(max_length=100)
    instructions = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (
            f"Recipe ID: {self.recipe_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Difficulty: {self.difficulty}\n"
            f"Duration: {self.duration}\n"
            f"Rating: {self.rating}\n"
            f"Created At: {self.created_at}\n"
            f"Last Updated: {self.updated_at}"
        )

# Recipe Ingredients
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe_ingredients')
    quantity = models.IntegerField()
    
    def __str__(self):
        return (
            f"Recipe: {self.recipe.title}\n"
            f"Ingredient: {self.ingredient.name}\n"
            f"Quantity: {self.quantity}"
        )

# Recipe User Saved
class RecipeUserSaved(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_user_saved')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_user_saved')
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return (
            f"User: {self.user.fname} {self.user.lname}\n"
            f"Recipe: {self.recipe.title}\n"
            f"Is Favorite: {'Yes' if self.is_favorite else 'No'}"
        )
        
# Recipe User Rating
class RecipeUserRating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_user_rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_user_rating')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return (
            f"User: {self.user.fname} {self.user.lname}\n"
            f"Recipe: {self.recipe.title}\n"
            f"Rating: {self.rating}\n" 
        )