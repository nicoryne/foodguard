from django.db import models
from django.utils import timezone
from datetime import date

# User
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11)
    date_of_birth = models.DateTimeField()
    
    @property
    def age(self):
        if self.date_of_birth is None:
            return None
        
        today = timezone.now().date()
        age = int (
            today.year
            - (self.date_of_birth.year)
            - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )
    
        return age
    
    def __str__(self):
        return (
            f"User ID: {self.user_id}\n"
            f"Name: {self.lname}, {self.fname}\n"
            f"Email: {self.email}\n"
            f"Phone #: {self.phone_number}\n"
            f"Birthdate: {self.date_of_birth}\n"
            f"Age: {self.age}"
        )
    
# Inventory
class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    ingredient_quantity = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='inventory')
    
    def __str__(self):
        return (
            f"Inventory ID: {self.inventory_id}\n"
            f"User: {self.user.fname} {self.user.lname}\n"
            f"Ingredient Quantity: {self.ingredient_quantity}\n"
            f"Last Updated: {self.updated_at}"
        )

# Ingredients
class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"Ingredient ID: {self.ingredient_id}\nName: {self.name}\nCategory: {self.category}"

# Inventory-Ingredient Ownership (Through Table)
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
    
    def __str__(self):
        return (
            f"Ingredient: {self.ingredient.name}\n"
            f"Quantity: {self.quantity}\n"
            f"Purchase Date: {self.purchase_date}\n"
            f"Expiry Date: {self.expiry_date}\n"
            f"Freshness: {self.freshness:.4f}"
        )
        
# Recipe
class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=35)
    duration = models.CharField(max_length=100)
    instructions = models.CharField(max_length=255)
    rating = models.IntegerField()
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

# Recipe Ingredients (Many-to-Many relationship through this model)
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

# Recipe User Saved (Tracks user’s saved recipes)
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

# Notification
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (
            f"Notification ID: {self.notification_id}\n"
            f"User: {self.user.fname} {self.user.lname}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Created At: {self.created_at}"
        )
    