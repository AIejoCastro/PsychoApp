from django.db import models
from django.contrib.auth.models import User
from db_connection import db

user_collection = db['user']

class HistorialResultado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sintomas = models.TextField()
    resultado = models.TextField()

    def __str__(self):
        return f"Historial de {self.usuario.username} - {self.fecha}"

class HistoriaClinica(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    antecedentes_medicos = models.TextField(blank=True, null=True)
    medicamentos_actuales = models.TextField(blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)
    contacto_emergencia = models.CharField(max_length=255)
    telefono_emergencia = models.CharField(max_length=15)

    def __str__(self):
        return f"Historia Clínica de {self.usuario.username}"