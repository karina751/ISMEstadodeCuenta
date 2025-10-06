# frontend/models.py

from django.db import models

# =================================================================
# 1. MODELO CLIENTE
#   Representa la persona o entidad que tiene el estado de cuenta.
# =================================================================
class Cliente(models.Model):
    # Campos que identifican al cliente
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    codigo_cliente = models.CharField(max_length=20, unique=True, verbose_name="Código de Cliente")
    
    # Campos de contacto (opcionales)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        # Representación amigable en el administrador de Django
        return f"{self.nombre} {self.apellido} ({self.codigo_cliente})"


# =================================================================
# 2. MODELO CUOTA
#   Representa una cuota a pagar o un pago realizado (registro en el estado de cuenta).
# =================================================================
class Cuota(models.Model):
    # Relación: Cada cuota pertenece a un Cliente (ForeignKey)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    
    # Datos de la transacción
    concepto = models.CharField(max_length=255)
    fecha_vencimiento = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Estado del pago
    pagada = models.BooleanField(default=False)
    fecha_pago = models.DateField(blank=True, null=True)
    
    # Comprobante de pago (Podría ser una URL o una ruta a un archivo PDF)
    comprobante_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.cliente.codigo_cliente} - {self.concepto} ({'Pagada' if self.pagada else 'Pendiente'})"

    # Clase Meta para ordenar las cuotas por fecha de vencimiento por defecto
    class Meta:
        ordering = ['fecha_vencimiento']