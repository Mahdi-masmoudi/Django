from django import forms
from .models import Produit
from .models import fournisseur
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class FournisseurForm(ModelForm):
    class Meta:
        model = fournisseur
        fields = "__all__"


class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email')
