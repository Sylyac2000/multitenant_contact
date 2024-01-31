"""Model.py of contact"""
from django.db import models
from django.contrib.auth.models import User




class Contact(models.Model):
    """Contact model."""
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom + ' ' + self.prenom


class Adresse(models.Model):
    """Adresse model for the address of a contact."""
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    commune = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    rue = models.CharField(max_length=100)
    adresse = models.TextField()
