from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

#models admin
class UserAdmin(BaseUserAdmin):
    model = get_user_model()
    list_display = ('username', 'email', 'name', 'is_staff')
    list_filter = ('is_staff', 'created_at')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name', 'email', 'image')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'name', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'email')
    search_help_text = _("Search by username or email.")
    ordering = ('username',)

# Register your models here.
admin.site.register(get_user_model(), UserAdmin)
