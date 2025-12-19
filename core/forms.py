from django import forms
from .models import Bolsa

class BolsaForm(forms.ModelForm):
    class Meta:
        model = Bolsa
        fields = ['nome']

