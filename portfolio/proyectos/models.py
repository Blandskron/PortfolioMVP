from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50, choices=[
        ('en_progreso', 'En Progreso'),
        ('finalizado', 'Finalizado'),
        ('pendiente', 'Pendiente')
    ])
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    