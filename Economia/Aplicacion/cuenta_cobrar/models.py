from django.db import models
from django.utils import timezone
# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    direccion = models.CharField(max_length=200, blank=True, null=True, verbose_name='Dirección')
    telefonos = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return "{}".format(self.nombre)


class Cabecera(models.Model):
    nombre = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Cliente')
    deuda = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto a diferir')
    fecha_cobro = models.DateField('Fecha inicio cobro', blank=False, null=False,default=timezone.now)
    meses_a_diferir = models.IntegerField(blank=False, null=False)
    saldo_interes = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Deuda')
    cuota_mensual = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='Cuota Mensual',default=0.00)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Cabecera"
        verbose_name_plural = "Cabeceras"
        ordering = ('nombre',)


class PagoDeuda(models.Model):
    cabecera = models.ForeignKey(Cabecera, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Cliente')
    abono = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Pago')
    fecha_ab = models.DateField('Fecha de pago',default=timezone.now,null = False,blank = False)

    def __str__(self):
        return "{} - {}".format(self.abono,self.cabecera)

    class Meta:
        pass


