from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, response
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import *
from Aplicacion.cuenta_cobrar.models import Cliente
from Aplicacion.cuenta_cobrar.forms import *
from weasyprint import HTML

# MENÚ
class MenuCobro(TemplateView):
    template_name = 'menu_seleccion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/'
        context['listar_url'] = '/menu'
        return context


# TABLA
class DetalleCliente(ListView):
    template_name = 'cliente/detalle_clientes.html'
    context_object_name = 'cliente'
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/cuenta_cobrar/tarjetas/'
        context['listar_url'] = '/cuenta_cobrar/tarjetas/'
        context['titulo'] = 'Registro de clientes'

        return context


# REGISTRO
class CrearCliente(CreateView):
    model = Cliente
    template_name = 'cliente/crearcliente.html'
    form_class = Clientes
    success_url = reverse_lazy("cuenta_cobrar:detalle_cliente")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registro de clientes'
        context['action_save'] = self.request.path
        context['url_anterior'] = '/cuenta_cobrar/tarjetas/'
        context['listar_url'] = '/cuenta_cobrar/detalle_cliente/'

        return context


class EliminarCliente(DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar_cliente.html'
    success_url = reverse_lazy('cuenta_cobrar:detalle_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Eliminar Registro de Clientes'
        context['url_anterior'] = '/cuenta_cobrar/detalle_cliente'
        context['listar_url'] = '/cuenta_cobrar/detalle_cliente'

        return context

class ActualizarCliente(UpdateView):
    model = Cliente
    template_name = "cliente/editar_cliente.html"
    success_url = reverse_lazy('cuenta_cobrar:detalle_cliente')
    form_class = Clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Actualizar Datos de Cliente'
        context['url_anterior'] = '/cuenta_cobrar/detalle_cliente'
        context['listar_url'] = '/cuenta_cobrar/detalle_cliente'

        return context

class CrearPdf(View):
     def get(self, request, *args, **kwargs):
         try:
            # Con el método 'get_template' llamamos al html que se convertirá en pdf
            # Se almacena en mi variable template que más adelante se usará
            template = get_template("plantillas_pdf/detalle_cliente.html")

            #Esto ya sabes Andy
            clientes = Cliente.objects.all()

            # Se manda mediante un context los datos que quieres pasar a tu plantilla HTML
            # Por eso estoy pasando una clave/valor, que 'clientes' tiene almacenado mis registros,
            # para después hacer un recorrido en mi plantilla
            context = {
                "titulo": "Listado de Clientes Registrados",
                "cliente": clientes
            }

            # Se crea una nueva variable para poder renderizar los context dentro de la plantilla
            # que anteriormente se llamó
            html = template.render(context)

            # 'HTML' Es una clase usada para importar 'Weasyprint' y recibe como parámetro
            # el archivo HTML, que está siendo almacenado en la variable 'html'
            # con 'write_pdf' lo convertirá en un archivo PDF
            pdf = HTML(string=html).write_pdf()

            # Se especifica el tipo de archivo que se presentará en el navegador
            # y no haya conflictos a la hora de renderizar
            response = HttpResponse(pdf, content_type='application/pdf')

            # attchment significa que se pueda descargar y visualizar en el mismo navegador
            # además de especificar un nombre al archivo mediante el 'filename'
            response['Content-Disposition'] = 'attachment; filename="ClientesRegistrados.pdf"'
            return response
         except:
             pass
         return HttpResponseNotFound('No se ha podido encontrar el pdf')






























