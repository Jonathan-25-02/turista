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
class Reservacion(models.Model):
    id_reservacion = models.AutoField(primary_key=True)
    turista = models.ForeignKey(Turista, on_delete=models.CASCADE, related_name='reservaciones')
    fecha_reservacion = models.DateField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    destino = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada')
    ], default='pendiente')

    def __str__(self):
        return f"Reservación {self.id_reservacion} - {self.turista.nombre} {self.turista.apellido}"     