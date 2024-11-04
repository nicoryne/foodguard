from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    
    # Index Path
    path('', TemplateView.as_view(template_name='index.html'), name='landing_page'),
    
    # Admin Path
    path('admin/', admin.site.urls),
    
    # Ingredient Path
    path('ingredient/', include('apps.ingredient.urls')),

    # Inventory Path
    path('inventory/', include('apps.inventory.urls')),
    
    # Notifications Path
    path('notifications/', include('apps.notifications.urls')),
    
    # Recipes Path
    path('recipes/', include('apps.recipes.urls')),
    
    # Shopping List Path
    path('shopping-list/', include('apps.shoppinglist.urls')),
    
    # Users Path
    path('users/', include('apps.users.urls')), 
]