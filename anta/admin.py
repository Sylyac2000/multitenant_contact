from django.contrib import admin


# Register your models here.
from anta.models import Contact
from tenants.utils.utility import tenant_from_request

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ['nom', 'prenom', 'email', 'telephone', 'created_by']
    list_display = ('nom', 'prenom', 'email', 'telephone',)


    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset

    def save_model(self, request, obj, form, change):
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)
