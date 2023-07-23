from django import forms
from EC.models import Courses

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = [
            'imagen',
            'titulo',
            'descripcion',
        ]