from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'tipo', 'price']

    tipo = forms.ChoiceField(choices=Flight.TIPO_CHOICES)