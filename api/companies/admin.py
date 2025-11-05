from django.contrib import admin
from django.db import transaction
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Admin configuration for Company model"""

    list_display = ('company_id', 'name', 'email', 'phone', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ['company_id', 'name', 'email']  # Enable autocomplete
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Company Information', {
            'fields': ('company_id', 'name', 'email', 'phone', 'address')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        """
        Override save_model to handle company_id updates properly.
        When company_id is changed, update the existing entity instead of creating a new one,
        and update all related contacts.
        """
        if change:  # This is an update, not a new creation
            # Get the original object from the database
            original_obj = Company.objects.get(pk=obj.pk)
            old_company_id = original_obj.company_id
            new_company_id = obj.company_id

            # Check if company_id was changed
            if old_company_id != new_company_id:
                # Import Contact here to avoid circular import
                from contacts.models import Contact

                with transaction.atomic():
                    # Update all related contacts to use the new company_id
                    Contact.objects.filter(company_id=old_company_id).update(
                        company_id=new_company_id
                    )

                    # Save the company with the updated company_id
                    super().save_model(request, obj, form, change)
            else:
                # No company_id change, just save normally
                super().save_model(request, obj, form, change)
        else:
            # This is a new company, save normally
            super().save_model(request, obj, form, change)
