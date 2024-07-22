from django.db import models

class Fernandez_Persona(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_de_registro = models.DateTimeField(auto_now_add=True)

    