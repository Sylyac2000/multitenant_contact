from django.shortcuts import render


from .models import Contact


def accueil(request):

    contacts = Contact.objects.all()

    print('contacts', contacts)

    context = {
        'contacts': contacts
    }
    return render(request, 'anta/home.html', context)


"""class ContactCreatePageView(CreateView):
    form_class = ContactForm
    template_name = 'anta/home.html'"""
