from django.db import models
from django.contrib.auth.models import User
from ..inventory.models import Ingredient
from django.db.models import Q, Count

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

@classmethod
def find_matching_recipes(cls, user_inventory):
    # Get ingredient IDs and their quantities in the user's inventory
    inventory_ingredients = user_inventory.ingredients.values('ingredient_id', 'quantity')

    # Create a dictionary for quick lookup of inventory quantities
    inventory_dict = {item['ingredient_id']: item['quantity'] for item in inventory_ingredients}

    # Query for matching recipes with a check for ingredient quantity
    matching_recipes = cls.objects.filter(
        recipe_ingredients__ingredient_id__in=inventory_dict.keys()
    ).annotate(
        match_count=Count(
            'recipe_ingredients',
            filter=Q(
                recipe_ingredients__ingredient_id__in=inventory_dict.keys(),
                recipe_ingredients__quantity__lte=models.F('recipe_ingredients__ingredient__quantity')
            )
        ),
        total_ingredients=Count('recipe_ingredients')
    ).annotate(
        ingredient_coverage=(
            Count(
                'recipe_ingredients',
                filter=Q(
                    recipe_ingredients__ingredient_id__in=inventory_dict.keys(),
                    recipe_ingredients__quantity__lte=models.F('recipe_ingredients__ingredient__quantity')
                )
            ) * 100.0 / Count('recipe_ingredients')
        )
    ).filter(
        match_count__gt=0
    ).order_by('-ingredient_coverage', '-match_count')

    return matching_recipes


# Recipe Ingredients
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe_ingredients')
    quantity = models.IntegerField()

# Recipe User Saved
class RecipeUserSaved(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_user_saved')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_user_saved')
    is_favorite = models.BooleanField(default=False)
        
# Recipe User Rating
class RecipeUserRating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_user_rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_user_rating')
    rating = models.DecimalField(max_digits=2, decimal_places=1)