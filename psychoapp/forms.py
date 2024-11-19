from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    direccion = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=15)
    antecedentes_medicos = forms.CharField(widget=forms.Textarea, required=False)
    medicamentos_actuales = forms.CharField(widget=forms.Textarea, required=False)
    alergias = forms.CharField(widget=forms.Textarea, required=False)
    contacto_emergencia = forms.CharField(max_length=255)
    telefono_emergencia = forms.CharField(max_length=15)

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(label="Correo electrónico", required=True)
    direccion = forms.CharField(max_length=255, label="Dirección", required=False)
    telefono = forms.CharField(max_length=15, label="Teléfono", required=False)
    antecedentes_medicos = forms.CharField(widget=forms.Textarea, label="Antecedentes médicos", required=False)
    medicamentos_actuales = forms.CharField(widget=forms.Textarea, label="Medicamentos actuales", required=False)
    alergias = forms.CharField(widget=forms.Textarea, label="Alergias", required=False)
    contacto_emergencia = forms.CharField(max_length=255, label="Contacto de emergencia", required=False)
    telefono_emergencia = forms.CharField(max_length=15, label="Teléfono de emergencia", required=False)

    class Meta:
        model = User
        fields = ['email', 'direccion', 'telefono', 'antecedentes_medicos', 'medicamentos_actuales', 'alergias', 'contacto_emergencia', 'telefono_emergencia']
