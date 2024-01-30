from django.shortcuts import render

from tenants.utils.utility import tenant_from_request, \
    set_tenant_schema_for_request, tenant_schema_from_request
from .models import Contact


def accueil(request):

    set_tenant_schema_for_request(request)
    tenant = tenant_schema_from_request(request)
    print('tenant', tenant)
    contacts = Contact.objects.all()

    print('contacts', contacts)

    context = {
        'contacts': contacts
    }
    return render(request, 'anta/home.html', context)


"""class ContactCreatePageView(CreateView):
    form_class = ContactForm
    template_name = 'anta/home.html'"""
