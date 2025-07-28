from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class AdminUser(UserAdmin):
    model = User
    list_display = ['username', 'email', 'profile', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {'fields': ('profile',)}),
    )

admin.site.register(User, AdminUser)