from django.utils import timezone
from django import forms
from .models import *
from .models import  Budget, Meeting, Phone
from .models import Souhaits


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
<<<<<<< HEAD
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


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['type', 'souhait', 'meet', 'montant']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['montant'].required = True
        self.fields['souhait'].required = False
        self.fields['meet'].required = False

        # Restreindre les choix pour le souhait et le meet à ceux de l'utilisateur connecté
        self.fields['souhait'].queryset = Souhaits.objects.filter(user=user, status='En cours de traitement')
        self.fields['meet'].queryset = Meeting.objects.filter(user=user, date_of_meeting__gte=timezone.now())

    def clean(self):
        cleaned_data = super().clean()
        type = cleaned_data.get('type')
        souhait = cleaned_data.get('souhait')
        meet = cleaned_data.get('meet')

        if type == 'souhait' and meet:
            raise forms.ValidationError("Le champ 'meet' ne doit pas être spécifié pour un budget de souhait.")
        elif type == 'meet' and souhait:
            raise forms.ValidationError("Le champ 'souhait' ne doit pas être spécifié pour un budget de meet.")

        return cleaned_data
=======
    
>>>>>>> Dia

