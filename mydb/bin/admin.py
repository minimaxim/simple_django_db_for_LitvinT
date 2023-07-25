from django.contrib import admin
from .models import User, Messanger
from .models import PhoneNumber


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number',)


admin.site.register(PhoneNumber, PhoneNumberAdmin)



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'phone', 'messanger')
    list_filter = ('messanger', 'phone', 'username', 'email')
    search_fields = ('name', 'email', 'phone', 'username')
    ordering = ('name', )


@admin.register(Messanger)
class MessangerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
