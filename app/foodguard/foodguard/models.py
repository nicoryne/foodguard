from django.db import models

# User
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phonenumber = models.CharField(max_length=11)
    dateofbirth = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.fname} {self.lname}"

# Inventory
class Inventory(models.Model):
    inventoryid = models.AutoField(primary_key=True)
    ingredient_quantity = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventories')

# Ingredients
class Ingredient(models.Model):
    ingredientid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Inventory-Ingredient Ownership (Through Table)
class InventoryIngredientOwnership(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    expiry_date = models.DateField()
    quantity = models.IntegerField()
    freshness = models.DecimalField(max_digits=5, decimal_places=4)

# Recipe
class Recipe(models.Model):
    recipeid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    instructions = models.CharField(max_length=255)
    rating = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Recipe Ingredients (Many-to-Many relationship through this model)
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

# Recipe User Saved (Tracks user’s saved recipes)
class RecipeUserSaved(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

# Shopping List
class ShoppingList(models.Model):
    shoppinglistid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_lists')
    capacity = models.IntegerField()

# Missing Ingredients (Tracks ingredients not in the inventory but in the recipe)
class MissingIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
