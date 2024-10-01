from django.db import models

# User
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phonenumber = models.CharField(max_length=11)
    dateofbirth = models.DateField()
    age = models.SmallIntegerField()

    def __str__(self):
        return f"{self.fname} {self.lname}"

# Inventory
class Inventory(models.Model):
    inventoryid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventories')

# Recipe
class Recipe(models.Model):
    recipeid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    isfavorite = models.BooleanField(default=False)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='recipes')

# Ingredients
class Ingredients(models.Model):
    ingredientid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    purchasedate = models.DateField()
    expirydate = models.DateField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    freshness = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='ingredients')

# Shopping List
class ShoppingList(models.Model):
    listid = models.AutoField(primary_key=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='shopping_lists')

# Recipe Ingredients
class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)

# Shopping List Ingredients
class ShoppingListIngredients(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)

# Missing Ingredients
class MissingIngredients(models.Model):
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
