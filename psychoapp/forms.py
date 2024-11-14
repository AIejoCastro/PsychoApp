from django import forms
from django.contrib.auth.models import User
from .models import HistoriaClinica

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    direccion = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=15)
    antecedentes_medicos = forms.CharField(widget=forms.Textarea, required=False)
    medicamentos_actuales = forms.CharField(widget=forms.Textarea, required=False)
    alergias = forms.CharField(widget=forms.Textarea, required=False)
    contacto_emergencia = forms.CharField(max_length=255)
    telefono_emergencia = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'fecha_nacimiento', 'direccion', 'telefono',
                  'antecedentes_medicos', 'medicamentos_actuales', 'alergias', 'contacto_emergencia', 'telefono_emergencia']