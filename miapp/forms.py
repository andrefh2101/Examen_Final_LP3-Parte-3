from django import forms
from .models import Fernandez_Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Fernandez_Persona
        fields = ['nombre', 'apellidos', 'sexo']
        widgets = {
            'sexo': forms.RadioSelect
        }
