from django.contrib import admin

# Register your models here.
from anta.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ['nom', 'prenom', 'email', 'telephone', 'created_by']
    list_display = ('nom', 'prenom', 'email', 'telephone',)


