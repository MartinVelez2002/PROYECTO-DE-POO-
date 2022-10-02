from .views.cuenta.views import *
from django.urls import path
from.views.cliente.views import *
from.views.menu.views import CobroTemplateView

app_name = "cuenta_cobrar"
urlpatterns = [
    # Menus
    # -- Principal
    path('menu/', CobroTemplateView.as_view(), name="menu"),
    # -- Secundaria
    path('tarjetas/', MenuCobro.as_view(), name="tarjetas"),

    # -- Cliente
    path('detalle_cliente/', DetalleCliente.as_view(), name="detalle_cliente"),
    path('crear_cliente/', CrearCliente.as_view(), name="crear_cliente"),
    path('eliminar_cliente/<int:pk>', EliminarCliente.as_view(), name="eliminar_cliente"),
    path('editar_cliente/<int:pk>', ActualizarCliente.as_view(), name="editar_cliente"),
    path('pdfclientes/', CrearPdf.as_view(), name="pdfclientes"),


    # Cuentas por Cobrar
    path('cobro/', DetalleListView.as_view(), name="cobro"),
    path('crearcuenta/', CrearCuenta.as_view(), name="crearcuenta"),
    path('crear/', CobroDeuda.as_view(), name="crear"),
    path('eliminar/<int:pk>', EliminarView.as_view(), name="eliminar"),
    path('pdfcuentas/', CrearCuentasPdf.as_view(), name="pdfcuentas"),

]