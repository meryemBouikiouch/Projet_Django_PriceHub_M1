from django import forms
from .models import Phone

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