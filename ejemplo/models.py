from django.db import models
import datetime

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fecha = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Passport:{self.numero_pasaporte}, Id:{self.id}, Fecha:{self.fecha}"

class  Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_registro = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"Nombre: {self.nombre}, Raza:{self.raza}, Id:{self.id}, Fecha:{self.fecha_registro}"


class Usuarios(models.Model):
    usuario = models.CharField(max_length = 30)
    contraseña = models.CharField(max_length = 30)
    nombre_apellido = models.CharField(max_length = 50)


