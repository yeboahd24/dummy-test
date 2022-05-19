from django_countries.widgets import CountrySelectWidget
from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['country']
        widgets = {
            'country': CountrySelectWidget(attrs={'class': 'custom-select d-block w-100'}),
        }