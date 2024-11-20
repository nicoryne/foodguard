from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.ingredient.models import Ingredient
from apps.shoppinglist.forms import IngredientToBuyForm
from .models import IngredientToBuy, ShoppingList

def shopping_list_view(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, shopping_list_id=list_id)
    ingredients_to_buy = shopping_list.ingredients_to_buy.all()
    ingredients = Ingredient.objects.all();

    total_items = ingredients_to_buy.count()
    items_in_cart = ingredients_to_buy.filter(in_cart=True).count()
    items_left = total_items - items_in_cart

    context = {
        'shopping_list': shopping_list,
        'ingredients': ingredients,
        'ingredients_to_buy': ingredients_to_buy,
        'total_items': total_items,
        'items_in_cart': items_in_cart,
        'items_left': items_left,
    }
    return render(request, 'shopping_list.html', context)

def finish_list(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, shopping_list_id=list_id)
    
    if request.method == "POST":
        shopping_list.clear_ingredients()
        shopping_list.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse('shoppinglist:list_detail', kwargs={'list_id': list_id})))
    
    return HttpResponseRedirect(reverse('shoppinglist:list_detail', kwargs={'list_id': list_id}))

def add_ingredient_to_buy(request, list_id):
    if request.method == 'POST':
        form = IngredientToBuyForm(request.POST)
        
        if form.is_valid():
            ingredient_to_buy = form.save(commit=False)
            ingredient_to_buy.shopping_list_id = list_id
            
            existing_ingredient = IngredientToBuy.objects.filter(
                shopping_list_id=list_id,
                ingredient_id=ingredient_to_buy.ingredient_id
            ).first()
            
            if existing_ingredient:
                existing_ingredient.quantity += ingredient_to_buy.quantity;
                existing_ingredient.save();
            else:
                ingredient_to_buy.save()
            

            ingredient_name = ingredient_to_buy.ingredient.name
            quantity = ingredient_to_buy.quantity

            return JsonResponse({
                'success': True,
                'ingredient_name': ingredient_name,
                'quantity': quantity
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'errors': 'Invalid method'})
    




