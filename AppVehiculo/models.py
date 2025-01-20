from django.db import models
from django.core.exceptions import ValidationError
import re

# Función para validar el VIN (17 caracteres)
def validar_vin(value):
    if len(value) != 17:
        raise ValidationError('El VIN debe tener exactamente 17 caracteres.')
    if not re.match(r'^[A-HJ-NPR-Z0-9]+$', value):
        raise ValidationError('El VIN solo puede contener caracteres alfanuméricos válidos.')

# Función para validar el CIS (7 dígitos + 1 dígito de verificación)
def validar_cis(value):
    if len(value) != 8:
        raise ValidationError('El CIS debe tener exactamente 8 caracteres.')
    if not value[:7].isdigit() or not value[7].isdigit():
        raise ValidationError('El CIS debe ser un número de 7 dígitos seguido de un dígito de verificación.')

# # Modelo para Vehiculo
class Vehiculo(models.Model):
    # VIN: alfanumérico de 17 caracteres
    vin = models.CharField(max_length=17, unique=True, validators=[validar_vin])
    
    # CIS: alfanumérico de 8 caracteres
    cis = models.CharField(max_length=8, validators=[validar_cis])
    
    # Version: alfanumérico de hasta 20 caracteres
    version = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Vehículo {self.vin} - {self.version}"
    



# class Vehiculo(models.Model):
#     vin = models.
#     nombre = models.CharField(max_length=100)
#     biografia = models.TextField()

#     def __str__(self):
        # return self.nombre