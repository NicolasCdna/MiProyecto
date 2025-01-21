
from django import forms
from .models import Vehiculo
from .models import Version
from .models import Proxy

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['vin', 'cis', 'version']  



class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['version_extend', 'version_codif', 'mercado']
        labels = {
            'version_extend': 'Versión Extendida',
            'version_codif': 'Código de Versión',
            'mercado': 'País de Destino',
        }
        widgets = {
            'version_extend': forms.TextInput(attrs={'maxlength': 10, 'placeholder': 'Máximo 10 caracteres'}),
            'version_codif': forms.TextInput(attrs={'maxlength': 3, 'placeholder': 'Exactamente 3 caracteres'}),
            'mercado': forms.Select(),
        }

class ProxyForm(forms.ModelForm):
    class Meta:
        model = Proxy
        fields = ['central', 'version', 'configuracion', 'sw_version']
        labels = {
            'central': 'Central',
            'version': 'Versión',
            'configuracion': 'Configuración (64 bits)',
            'sw_version': 'Versión de Software',
        }
    configuracion = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 64}))