from django.contrib import admin

from .models import User, Messanger


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'phone', 'messanger')
    list_filter = ('messanger', 'phone', 'username', 'email')
    search_fields = ('name', 'email', 'phone', 'username')
    ordering = ('name', )


@admin.register(Messanger)
class MessangerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
