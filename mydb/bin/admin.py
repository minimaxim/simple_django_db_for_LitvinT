from django.contrib import admin

from .models import User, Company


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'country', 'email', 'phone', 'login_bitmain', 'telegram_link', 'instagram_link', 'twitter_link',
        'vk_link', 'facebook_link', 'linkedin_link', 'whatsapp_link'
    )
    list_filter = ('telegram_link', 'instagram_link', 'twitter_link', 'vk_link', 'facebook_link', 'linkedin_link', 'whatsapp_link')
    search_fields = ('id', )

    # ordering = ('is_published', 'name', 'slug')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'first_fiz', 'second_fiz', 'phone', 'other_phone')
