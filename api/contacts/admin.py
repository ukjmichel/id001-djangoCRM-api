from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin configuration for Contact model"""

    list_display = ('first_name', 'last_name', 'email', 'company', 'position', 'created_at')
    list_filter = ('created_at', 'updated_at', 'company')
    search_fields = ('first_name', 'last_name', 'email', 'company__name', 'company__company_id')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('company',)

    fieldsets = (
        ('Contact Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'position')
        }),
        ('Company', {
            'fields': ('company',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
