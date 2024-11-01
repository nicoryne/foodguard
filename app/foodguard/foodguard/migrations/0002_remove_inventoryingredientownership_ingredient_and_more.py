# Generated by Django 5.1.2 on 2024-10-29 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodguard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryingredientownership',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='ingredientincart',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='ingredienttobuy',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='ingredientincart',
            name='shopping_list',
        ),
        migrations.RemoveField(
            model_name='ingredienttobuy',
            name='shopping_list',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='inventoryingredientownership',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='recipeusersaved',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='recipeusersaved',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='IngredientInCart',
        ),
        migrations.DeleteModel(
            name='IngredientToBuy',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
        migrations.DeleteModel(
            name='InventoryIngredientOwnership',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='RecipeIngredient',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.DeleteModel(
            name='RecipeUserSaved',
        ),
        migrations.DeleteModel(
            name='ShoppingList',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
