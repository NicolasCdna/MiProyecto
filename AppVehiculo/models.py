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

class Version(models.Model):
    # Campo alfanumérico de máximo 10 caracteres
    version_extend = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="Versión Extendida"
    )
    
    # Campo alfanumérico - 3 caracteres
    version_codif = models.CharField(
        max_length=3,
        unique=True,
        verbose_name="Código de Versión"
    )
    
    # Lista de opciones para el campo país de destino
    MERCADO_CHOICES = [
        ('EU', 'Europa'),
        ('AS', 'Asia'),
        ('AM', 'América'),
        ('AF', 'África'),
        ('OC', 'Oceanía'),
        ('AR', 'Argentina'),
    ]
    mercado = models.CharField(
        max_length=2,
        choices=MERCADO_CHOICES,
        verbose_name="País de Destino"
    )
    
    class Meta:
        # Constraint para relación biunívoca
        unique_together = ('version_extend', 'version_codif')
        verbose_name = "Versión"
        verbose_name_plural = "Versiones"
    
    def __str__(self):
        return f"{self.version_codif} - {self.version_extend} ({self.get_mercado_display()})"
    
    #Definimos Proxy, que toma informacion de la clase Version.
    
from .models import Version  # Asegúrate de que el modelo Version esté importado

class Proxy(models.Model):
    # Opciones para Centrales (ECUs básicas)
    ECU_CHOICES = [
        ('BCM', 'Body Control Module'),
        ('PCM', 'Powertrain Control Module'),
        ('TCM', 'Transmission Control Module'),
        ('ECM', 'Engine Control Module'),
        ('ABS', 'Anti-lock Braking System'),
    ]
    central = models.CharField(
        max_length=3,
        choices=ECU_CHOICES,
        verbose_name="Central"
    )
    
    # Relación con Version
    version = models.ForeignKey(
        Version,
        on_delete=models.CASCADE,
        verbose_name="Versión"
    )
    
    # Campo de configuración (64 bits como cadena)
    configuracion = models.CharField(
        max_length=64,
        verbose_name="Configuración"
    )
    
    # Versión de software
    sw_version = models.CharField(
        max_length=10,
        verbose_name="Versión de Software"
    )
    
    class Meta:
        verbose_name = "Proxy"
        verbose_name_plural = "Proxies"
    
    def __str__(self):
        return f"{self.central} - {self.version} - SW: {self.sw_version}"

