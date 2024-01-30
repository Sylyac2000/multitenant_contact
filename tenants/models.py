"""tenants models"""
from django.db import models


# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"

    def __str__(self):
        return self.name + self.subdomain_prefix

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True