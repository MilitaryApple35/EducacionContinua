from django import forms
from EC.models import *

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = [
            'imagen',
            'titulo',
            'descripcion',
        ]

class ConferenciasForm(forms.ModelForm):
    class Meta:
        model = Conferencias
        fields = [
            'imagen',
            'titulo',
            'descripcion',
        ]

class TalleresForm(forms.ModelForm):
    class Meta:
        model = Talleres
        fields = [
            'imagen',
            'titulo',
            'descripcion',
        ]

class DiplomadosForm(forms.ModelForm):
    class Meta:
        model = Diplomados
        fields = [
            'imagen',
            'titulo',
            'descripcion',
        ]

class CongresosForm(forms.ModelForm):
    class Meta:
        model = Congresos
        fields = [
            'imagen',
            'titulo',
            'descripcion',
        ]

class CapacitacionesForm(forms.ModelForm):
    class Meta:
        model = Capacitaciones
        fields = [
            'imagen',
            'titulo',
            'descripcion',
        ]