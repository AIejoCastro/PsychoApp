from django.db import models
from django.contrib.auth.models import User

class HistorialResultado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sintomas = models.TextField()
    resultado = models.TextField()

    def __str__(self):
        return f"Historial de {self.usuario.username} - {self.fecha}"
