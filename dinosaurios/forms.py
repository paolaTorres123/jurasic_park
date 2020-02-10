from .models import Periodo, Dinosaurio,LONGUITUD_MAXIMA
from django.forms import ModelForm,Textarea, TextInput


class PeriodoForm(ModelForm):

    class Meta:
        model = Periodo
        fields = '__all__'

        widgets = {
            'descripcion': Textarea(attrs={'cols': 6, 'rows': 2,'class':'form-control'}),
            'nombre':TextInput(attrs={'class':'form-control'}),
        }

        error_messages = {
            'nombre' : {'max_length': 'Error de longitud', 'required': 'Se requiere'}
        }

class DinoForm(ModelForm):

    class Meta:
        model = Dinosaurio
        fields = '__all__'

        error_messages = {
            'nombre' : {'max_length': LONGUITUD_MAXIMA, 'required': 'Se requiere'}
        }