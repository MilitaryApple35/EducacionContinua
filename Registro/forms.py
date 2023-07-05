from django import forms
from EC.models import Registro

class RegistroForm(forms.ModelForm):
    procedencia = forms.ChoiceField(choices=(('Estudiante', 'Estudiante UPSIN'), ('Egresado', 'Egresado UPSIN'), ('Externo', 'Externo a UPSIN')))
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
        
