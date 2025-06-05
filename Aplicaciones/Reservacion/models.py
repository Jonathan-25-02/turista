from django.db import models
class Turista(models.Model):
    id_turista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.nacionalidad})"
# Create your models here.
