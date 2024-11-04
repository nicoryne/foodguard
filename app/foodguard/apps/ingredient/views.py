from .models import Ingredient
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Ingredient List View
class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredient_list.html'
    context_object_name = 'ingredients'

# Ingredient Detail View
class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'ingredient_detail.html'
    context_object_name = 'ingredient'

# # Ingredient Create View
# class IngredientCreateView(CreateView):
#     model = Ingredient
#     fields = ['name', 'category', 'image']
#     template_name = 'ingredient_create_form.html'
#     success_url = '/ingredients/'

class IngredientCreateView(CreateView):
    model = Ingredient
    fields = ['name', 'quantity', 'category', 'image', 'date_purchased', 'expiry_date'] 
    template_name = 'ingredient_create_form.html'
    success_url = reverse_lazy('ingredient-list')

# Ingredient Update View
class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = ['name', 'category', 'image']
    template_name = 'ingredient_update_form.html'
    success_url = '/ingredients/'

# Ingredient Delete View
class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'ingredient_confirm_delete.html'
    success_url = '/ingredients/'
