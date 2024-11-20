from .models import Ingredient
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import timedelta
from django.utils.timezone import now

# Ingredient List View
class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredient_list.html'
    context_object_name = 'ingredients'

    def get_context_data(self, **kwargs):
        # Call the parent class method to get the default context
        context = super().get_context_data(**kwargs)
        
        # Filter urgent ingredients (expiry_date is within 4 days from date_purchased)
        urgent_ingredients = Ingredient.objects.filter(
            date_purchased__isnull=False,
            expiry_date__isnull=False,
            expiry_date__lte=(now().date() + timedelta(days=4))
        )
        
        # Add urgent ingredients to the context
        context['urgent_ingredients'] = urgent_ingredients
        return context

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
# views.py
class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = ['name', 'quantity', 'category', 'image', 'date_purchased', 'expiry_date']
    template_name = 'ingredient_update_form.html'
    success_url = reverse_lazy('ingredient-list')

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'ingredient_confirm_delete.html'
    success_url = reverse_lazy('ingredient-list')

