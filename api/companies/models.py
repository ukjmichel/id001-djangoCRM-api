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
