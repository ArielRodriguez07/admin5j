from django.db import models

# Create your models here.

class AlumnoTabla(models.Model):
    Apaterno=models.CharField(max_length=50, verbose_name="Apellido paterno")
    Amaterno=models.CharField(max_length=50,verbose_name="Apellido Materno")
    nombres=models.CharField(max_length=100,verbose_name="Nombre (S)")
    fecha_nacimiento=models.DateField(verbose_name="Fecha de nacimiento",null=False,blank=False)
