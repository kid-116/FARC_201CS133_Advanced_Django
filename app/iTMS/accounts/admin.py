from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
    )
    search_fields = (
        'username',
        'email',
    )
    readonly_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
        'last_login',
        'created_at',
        'updated_at',
        'is_active',
        'is_staff',
        'is_admin',
    )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
