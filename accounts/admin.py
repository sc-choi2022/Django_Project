from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'phone_number',
        'password',
    )

admin.site.register(User, UserAdmin)