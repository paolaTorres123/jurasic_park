from django.db import models
from django.core.validators import MaxLengthValidator
from dinosaurios.validador import validar_altura

LONGUITUD_MAXIMA='Error en la longutud'

class Periodo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField("Descripción", null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Dinosaurio(models.Model):
     nombre = models.CharField(max_length=100,validators=[MaxLengthValidator(100,LONGUITUD_MAXIMA)])
     altura = models.DecimalField(max_digits=5, decimal_places=2,validators=[validar_altura])
     periodo = models.ForeignKey(Periodo, verbose_name='Periodo', on_delete=models.CASCADE)
     #El upload_to crea dentro del Media el directorio dino. 
     imagen = models.ImageField("Imagen", upload_to='dinos', null=True, blank=True)

     def __str__(self):
        return self.nombre