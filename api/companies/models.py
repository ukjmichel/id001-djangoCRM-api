from django.db import models


class Company(models.Model):
    """Company model for CRM"""
    company_id = models.CharField(max_length=100, unique=True, help_text="Unique company identifier")
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.company_id} - {self.name}"


class Contact(models.Model):
    """Contact model for CRM"""
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='contacts',
        to_field='company_id',
        help_text="Associated company"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.company.company_id})"
