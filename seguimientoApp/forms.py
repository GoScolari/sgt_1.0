from django import forms
from .models import Vehiculo, Incidencia, Mantenimiento

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        widgets = {
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date'}),
            'ano_fabricacion': forms.DateInput(attrs={'type': 'date'}),
        }

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'comentario': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Ingrese su comentario aquí'}),
        }
        
class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type':'date',}), 

        }