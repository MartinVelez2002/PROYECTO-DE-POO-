from Economia.wsgi import get_wsgi_application
from Aplicacion.cuenta_cobrar.models import Cliente
from django.template.loader import get_template


print("Todo bien")

# def Imp_detail_cli():
#     # Llamaos a mi template con el método 'get_template'
#     cliente = get_clientes()
#     template = get_template("plantillas_pdf/detalle_cliente.html")
#     context = {"name": "POR FAVOR FUNCIONA - 23:01 ", 'cliente': cliente}
#
#     # Permite recibir los datos enviados mediante un context
#     html_template = template.render(context)
#     HTML(string=html_template).write_pdf(target="a.pdf")
#
#
# def get_clientes():
#     clientes = Cliente.objects.all()
#     return clientes
#
#
#
# Imp_detail_cli()