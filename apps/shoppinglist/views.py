import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.ingredient.models import Ingredient
from django.contrib.auth.models import User
from apps.shoppinglist.forms import IngredientToBuyForm
from .models import IngredientToBuy, ShoppingList

from apps.notifications.models import Notification

def shopping_list_view(request):
    userr = get_object_or_404(User, email=request.user.email);
    shopping_list = get_object_or_404(ShoppingList, user=userr)
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

def finish_list(request):
    userr = get_object_or_404(User, email=request.user.email);
    shopping_list = get_object_or_404(ShoppingList, user=userr)
    
    if request.method != "POST":
        return HttpResponseRedirect(reverse('shoppinglist:list_detail'))
    
    Notification.objects.create(
            user=userr,
            title="Shopping list cleared!",
            description=f"You just recently cleared your shopping list."
        )
    
    shopping_list.clear_ingredients()
    shopping_list.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse('shoppinglist:list_detail')))
    
def add_ingredient_to_buy(request):
    userr = get_object_or_404(User, email=request.user.email);
    shopping_list = get_object_or_404(ShoppingList, user=userr)
    list_id = shopping_list.shopping_list_id;
    
    if request.method != "POST":
        return HttpResponseRedirect(reverse('shoppinglist:list_detail'))
    
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

        return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse('shoppinglist:list_detail')))

def delete_ingredient_to_buy(request):
    userr = get_object_or_404(User, email=request.user.email);
    shopping_list = get_object_or_404(ShoppingList, user=userr)

    if request.method != "POST":
        return JsonResponse({'success': False})
    
    data = json.loads(request.body)
    selected_ingredients_ids = data.get('selected_ingredients', [])

    if not selected_ingredients_ids:
        return JsonResponse({'success': False})

    for ingredient_id in selected_ingredients_ids:
        ingredient = shopping_list.ingredients_to_buy.get(ingredient_id=ingredient_id)
        ingredient.delete()

    return JsonResponse({'success': True})
    
 
def toggle_to_cart(request, ingredient_id):    
    userr = get_object_or_404(User, email=request.user.email);
    shopping_list = get_object_or_404(ShoppingList, user=userr)
    
    if request.method != "POST":
        return HttpResponseRedirect(reverse('shoppinglist:list_detail', user=request.user))
    
    ingredient = shopping_list.ingredients_to_buy.get(ingredient_id=ingredient_id)

    if not ingredient:
        return HttpResponseRedirect(reverse('shoppinglist:list_detail'))
    
    ingredient.in_cart = not ingredient.in_cart
    ingredient.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse('shoppinglist:list_detail')))

def quantity_change(request, ingredient_id, is_add):
    userr = get_object_or_404(User, email=request.user.email);
    shopping_list = get_object_or_404(ShoppingList, user=userr)
    
    if request.method != "POST":
        return HttpResponseRedirect(reverse('shoppinglist:list_detail'))
    
    ingredient = shopping_list.ingredients_to_buy.get(ingredient_id=ingredient_id)
    
    if not ingredient:
        return HttpResponseRedirect(reverse('shoppinglist:list_detail'))
    
    if is_add == 1:
        ingredient.quantity += 1;
    else:
        ingredient.quantity -=1;

    if ingredient.quantity <= 0:
        ingredient.delete()
    else:
        ingredient.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse('shoppinglist:list_detail')))
        



        
        
        



