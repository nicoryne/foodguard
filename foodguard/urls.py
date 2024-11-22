from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    
    # Index Path
    path('', TemplateView.as_view(template_name='landing.html'), name='landing_page'),
    
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
    path('recipe_list/', include('apps.recipes.urls')),
    
    # Shopping List Path
    path('shoppinglist/', include('apps.shoppinglist.urls')),
    
    # Users Path
    path('users/', include('apps.users.urls')), 
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)