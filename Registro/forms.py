from django import forms
from EC.models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = [
            'Nombres',
            'Apellidos',
            'Email',
            'Curso',
            'Procedencia',
            'Institucion',
            'Matricula',
            'Estado',
            'Pais',
            'Municipio',
            'EstadoCivil',
        ]