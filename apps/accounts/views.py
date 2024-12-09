from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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


def profile(request):
    userr = get_object_or_404(User, email=request.user.email);
    profile = Profile.objects.get(user=userr)
    return render(request, 'profile.html', { "profile" : profile });
    
@login_required
def edit_profile(request):
    profile = request.user.profile 
    if request.method == "POST":
        profile.user.first_name = request.POST.get('first_name')
        profile.user.last_name = request.POST.get('last_name')
        profile.user.email = request.POST.get('email')
        profile.phone_number = request.POST.get('phone_number')
        profile.date_of_birth = request.POST.get('birthdate')
        profile.user.save()
        profile.save()
        messages.success(request, "Profile updated successfully!")

        return redirect('accounts:profile')
    return render(request, 'accounts:profile', {'profile': profile})