from django import forms
from django.utils import timezone
from django.forms import ModelForm
from Aplicacion.cuenta_cobrar.models import *


class CabeceraForm(ModelForm):
    class Meta:
        model = Cabecera
        fields = '__all__'
        widgets = {
            'nombre': forms.Select(attrs={'class': 'form-control ', 'id': 'nom'}),
            'deuda': forms.NumberInput(attrs={'class': 'form-control', 'id': 'deu'}),
            'fecha_cobro': forms.DateInput(format=('%d/%m/%Y'),
                                    attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha', 'type': 'date','id':'fecha'}),
            'meses_a_diferir': forms.NumberInput(attrs={'class': 'form-control', 'id': 'mes'}),
            'saldo_interes':forms.NumberInput(attrs={'class': 'form-control', 'id':'saldo', 'readonly': True}),
            'cuota_mensual':forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'id': 'cuotamen'}),
        }


class PagoDeudaForm(ModelForm):
    class Meta:
        model = PagoDeuda
        fields = '__all__'
        widgets = {

            'abono':forms.NumberInput(attrs= {'placeholder': 'Ingrese el valor de pago','class':'form-control','id':'pago'}),
            'fecha_ab': forms.DateInput(format=('%d/%m/%Y'),
                                        attrs={'class': 'form-control', 'type': 'date'}),
            'cabecera':forms.Select(attrs={'class':'form-control'})
        }

class Clientes(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {

          'telefonos': forms.NumberInput(attrs={'placerholder': 'Ingrese su número de teléfono'}),
          'fecha': forms.DateInput(
                         format=('%Y-%m-%d'),
                         attrs={'class': 'form-control', 'type': 'date'}
          ),
        }