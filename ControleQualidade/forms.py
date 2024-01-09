from django import forms
from .models import LoteAco, EnsaioMecanico

class LoteAcoForm(forms.ModelForm):
    class Meta:
        model = LoteAco
        fields = '__all__'

class EnsaioMecanicoForm(forms.ModelForm):
    class Meta:
        model = EnsaioMecanico
        fields = '__all__'