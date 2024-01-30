"""Admin for registering models"""
from django.contrib import admin

from tenants.models import Tenant


@admin.register(Tenant)
class Tenant(admin.ModelAdmin):
    list_display = ('name', 'subdomain_prefix')
