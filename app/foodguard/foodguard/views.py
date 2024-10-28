from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User, Inventory, Ingredient, InventoryIngredientOwnership, Recipe, RecipeIngredient, RecipeUserSaved, ShoppingList, MissingIngredient
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# User List View
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

# User Detail View
class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

# Create a New User
class UserCreateView(CreateView):
    model = User
    fields = ['fname', 'lname', 'password', 'email', 'phonenumber', 'dateofbirth', 'age']
    template_name = 'user_form.html'
    success_url = '/users/'

# Inventory List View
class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory_list.html'
    context_object_name = 'inventories'

# Inventory Detail View
class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory_detail.html'
    context_object_name = 'inventory'

# Add Ingredients to Inventory (Create View)
class InventoryIngredientCreateView(CreateView):
    model = InventoryIngredientOwnership
    fields = ['ingredient', 'inventory', 'purchase_date', 'expiry_date', 'quantity', 'freshness']
    template_name = 'inventory_ingredient_form.html'
    success_url = '/inventory/'

# Recipe List View
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

# Recipe Detail View
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'

# Create New Recipe
class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'description', 'instructions', 'rating']
    template_name = 'recipe_form.html'
    success_url = '/recipes/'

# Save a Recipe (User Save View)
def save_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    user = request.user  # Assuming user is logged in
    RecipeUserSaved.objects.create(user=user, recipe=recipe, is_favorite=False)
    return redirect('recipe_list')

# Shopping List View
class ShoppingListView(ListView):
    model = ShoppingList
    template_name = 'shopping_list.html'
    context_object_name = 'shopping_lists'

# Add Ingredient to Shopping List
class ShoppingListIngredientCreateView(CreateView):
    model = ShoppingList
    fields = ['user', 'capacity']
    template_name = 'shopping_list_form.html'
    success_url = '/shopping-lists/'

# Handle Missing Ingredients
def missing_ingredients(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    missing = MissingIngredient.objects.filter(inventory=inventory)
    return render(request, 'missing_ingredients.html', {'missing': missing})