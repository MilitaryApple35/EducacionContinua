from django import forms
from EC.models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = [
            'nombres',
            'apellidos',
            'email',
            'curso',
            'procedencia',
            'Institucion',
            'Matricula',
            'estado',
            'pais',
            'municipio',
            'estadocivil',
            'Carrera',
        ]
