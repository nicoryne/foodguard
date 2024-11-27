from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render

from apps.accounts.forms import RegisterForm
from .models import Profile
from ..inventory.models import Inventory
from ..shoppinglist.models import ShoppingList

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Initialize Profile
            Profile.objects.create(
                user=user,
                date_of_birth=form.cleaned_data.get('date_of_birth'),
                phone_number=form.cleaned_data.get('phone_number'),
            )
            
            # Initialize Inventory & Shopping List
            Inventory.objects.create(user=user)
            ShoppingList.objects.create(user=user)
            
            return redirect('accounts:login') 
        else:
            print(form.errors.as_data())
            print(form.non_field_errors())
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})
    
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
    
    