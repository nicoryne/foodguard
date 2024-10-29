from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Recipe, RecipeIngredient, RecipeUserSaved, RecipeUserRating

@receiver(post_save, sender=Recipe)
def log_recipe_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New recipe created: {instance.title}")
    else:
        print(f"Recipe updated: {instance.title}")

@receiver(pre_delete, sender=Recipe)
def log_recipe_deletion(sender, instance, **kwargs):
    print(f"Recipe deleted: {instance.title}")

@receiver(post_save, sender=RecipeIngredient)
def log_recipe_ingredient_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New ingredient added to recipe: {instance.recipe.title} - Ingredient: {instance.ingredient.name}")

@receiver(pre_delete, sender=RecipeIngredient)
def log_recipe_ingredient_deletion(sender, instance, **kwargs):
    print(f"Ingredient removed from recipe: {instance.recipe.title} - Ingredient: {instance.ingredient.name}")

@receiver(post_save, sender=RecipeUserSaved)
def log_recipe_user_saved(sender, instance, created, **kwargs):
    if created:
        print(f"User saved recipe: {instance.recipe.title} - User: {instance.user.fname} {instance.user.lname}")

@receiver(pre_delete, sender=RecipeUserSaved)
def log_recipe_user_saved_deletion(sender, instance, **kwargs):
    print(f"User removed recipe from favorites: {instance.recipe.title} - User: {instance.user.fname} {instance.user.lname}")

@receiver(post_save, sender=RecipeUserRating)
def log_recipe_user_rating(sender, instance, created, **kwargs):
    if created:
        print(f"User rated recipe: {instance.recipe.title} - User: {instance.user.fname} {instance.user.lname} - Rating: {instance.rating}")

@receiver(pre_delete, sender=RecipeUserRating)
def log_recipe_user_rating_deletion(sender, instance, **kwargs):
    print(f"User removed rating from recipe: {instance.recipe.title} - User: {instance.user.fname} {instance.user.lname}")
