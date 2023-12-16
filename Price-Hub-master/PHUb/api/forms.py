from django import forms
from .models import *

class AdvancedSearchForm(forms.Form):
    nom = forms.CharField(required=False)
    prix_min = forms.DecimalField(required=False)
    prix_max = forms.DecimalField(required=False)
    ram_min = forms.IntegerField(required=False)
    ram_max = forms.IntegerField(required=False)
    operating_system = forms.CharField(required=False)
    storage_min = forms.IntegerField(required=False)
    storage_max = forms.IntegerField(required=False)
    brand = forms.CharField(max_length=50, required=False, label='Marque')


class AddPhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
class Sujet_telephoneForm(forms.ModelForm):
    class Meta:
        model = Sujet_telephone
        fields = ['titre', 'description']

class Commentaire_telephoneForm(forms.ModelForm):
    class Meta:
        model = Commentaire_telephone
        fields = ['texte']


class Sujet_tabletteForm(forms.ModelForm):
    class Meta:
        model = Sujet_tablette
        fields = ['titre', 'description']

class Commentaire_tabletteForm(forms.ModelForm):
    class Meta:
        model = Commentaire_tablette
        fields = ['texte']


class Sujet_ordinateurForm(forms.ModelForm):
    class Meta:
        model = Sujet_ordinateur
        fields = ['titre', 'description']

class Commentaire_ordinateurForm(forms.ModelForm):
    class Meta:
        model = Commentaire_ordinateur
        fields = ['texte']


class Sujet_Accessoire_telephoneForm(forms.ModelForm):
    class Meta:
        model = Sujet_Accessoire_telephone
        fields = ['titre', 'description']

class Commentaire_Accessoire_telephoneForm(forms.ModelForm):
    class Meta:
        model = Commentaire_Accessoire_telephone
        fields = ['texte']


class Sujet_Accessoire_ordinateurForm(forms.ModelForm):
    class Meta:
        model = Sujet_Accessoire_ordinateur
        fields = ['titre', 'description']

class Commentaire_Accessoire_ordinateurForm(forms.ModelForm):
    class Meta:
        model = Commentaire_Accessoire_ordinateur
        fields = ['texte']



class Sujet_Accessoire_tabletteForm(forms.ModelForm):
    class Meta:
        model = Sujet_Accessoire_tablette
        fields = ['titre', 'description']

class Commentaire_Accessoire_tabletteForm(forms.ModelForm):
    class Meta:
        model = Commentaire_Accessoire_tablette
        fields = ['texte']