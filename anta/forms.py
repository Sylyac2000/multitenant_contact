""""Forms"""

from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):

    class Meta:
        model = Contact

        fields = ('nom', 'prenom', 'email', 'telephone', 'created_by')