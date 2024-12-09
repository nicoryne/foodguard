from .models import Ingredient
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.timezone import now

import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from apps.inventory.models import InventoryIngredientOwnership, Inventory
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone



def ingredient_list_view(request):
    user = get_object_or_404(User, email=request.user.email)

    ingredients = Ingredient.objects.filter(
        ingredient_id__in=InventoryIngredientOwnership.objects.filter(inventory__user=user).values('ingredient_id')
    )

    today = timezone.now().date()

    urgent_ingredients = ingredients.filter(
        expiry_date__lte=today + timedelta(days=4),
        expiry_date__gte=today
    )

    context = {
        'ingredients': ingredients,
        'total_ingredients': ingredients.count(),
        'urgent_ingredients': urgent_ingredients,
    }

    return render(request, 'ingredient_list.html', context)

def create_ingredient(request):
    user = get_object_or_404(User, email=request.user.email)
    inventory = get_object_or_404(Inventory, user=user)

    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        date_purchased = request.POST.get('date_purchased')
        expiry_date = request.POST.get('expiry_date')

        if not name:
            return JsonResponse({'error': 'Name is required'}, status=400)

        ingredient = Ingredient.objects.create(
            name=name,
            quantity=quantity,
            category=category,
            image=image,
            date_purchased=date_purchased,
            expiry_date=expiry_date
        )

        InventoryIngredientOwnership.objects.create(
            ingredient=ingredient,
            inventory=inventory,
            purchase_date=date_purchased,
            expiry_date=expiry_date,
            quantity=quantity
        )

        return HttpResponseRedirect(reverse_lazy('ingredient:ingredient-list'))  # Redirect to ingredient list view after creation

    return render(request, 'ingredient_create_form.html')



# Ingredient List
class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredient_list.html'
    context_object_name = 'ingredients'

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    user = get_object_or_404(User, email=self.request.user.email)
    inventory = get_object_or_404(Inventory, user=user)
    user_ingredients = InventoryIngredientOwnership.objects.filter(inventory=inventory)
    ingredients_in_inventory = Ingredient.objects.filter(ingredient_id__in=user_ingredients.values('ingredient_id'))
    urgent_ingredients = ingredients_in_inventory.filter(
        date_purchased__isnull=False,
        expiry_date__isnull=False,
        expiry_date__lte=(now().date() + timedelta(days=4))
    )
    context['ingredients_in_inventory'] = ingredients_in_inventory
    context['urgent_ingredients'] = urgent_ingredients

    return context

# Ingredient Detail View
class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'ingredient_detail.html'
    context_object_name = 'ingredient'

# Ingredient Update View
# views.py
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = ['name', 'quantity', 'category', 'image', 'date_purchased', 'expiry_date']
    template_name = 'ingredient_update_form.html'
    success_url = reverse_lazy('ingredient:ingredient-list')

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'ingredient_confirm_delete.html'
    success_url = reverse_lazy('ingredient:ingredient-list')

