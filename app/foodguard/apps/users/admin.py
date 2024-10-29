from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'fname', 'lname', 'email', 'phone_number', 'age')
    search_fields = ('fname', 'lname', 'email')
    list_filter = ('date_of_birth',)
    ordering = ('lname',)
