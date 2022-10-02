from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import DeleteView,ListView,CreateView, TemplateView, View
from Aplicacion.cuenta_cobrar.models import Cabecera,PagoDeuda
from Aplicacion.cuenta_cobrar.forms import CabeceraForm,PagoDeudaForm
from weasyprint import HTML


class DetalleListView(ListView):
    template_name = "main_cobro.html"
    context_object_name = 'cobro'
    model = Cabecera


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/cuenta_cobrar/tarjetas'
        context['listar_url'] = '/menu'
        context['titulo'] = 'Cuentas por Cobrar'
        context['registro'] = PagoDeuda.objects.filter()
        return context


class CrearCuenta(CreateView):
    model = Cabecera
    template_name = "pantallas/registros.html"
    success_url = reverse_lazy('cuenta_cobrar:cobro')
    form_class = CabeceraForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/cuenta_cobrar/crearcuenta/'
        context['titulo'] = 'Crear Registro'
        context['url_anterior'] = '/cuenta_cobrar/cobro'
        context['listar_url'] = '/cuenta_cobrar/cobro'
        return context




class CobroDeuda(CreateView):
    model = PagoDeuda
    form_class = PagoDeudaForm
    template_name = "pantallas/pago_deuda.html"
    success_url = reverse_lazy('cuenta_cobrar:cobro')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/cuenta_cobrar/crear/'
        context['titulo'] = 'Sección para realizar el pago'
        context['url_anterior'] = '/cuenta_cobrar/cobro'
        context['listar_url'] = '/cuenta_cobrar/cobro'
        return context




class EliminarView(DeleteView):
    model = Cabecera
    template_name = "pantallas/eliminar.html"
    success_url = reverse_lazy('cuenta_cobrar:cobro')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Eliminar Registros'
        context['url_anterior'] = '/cuenta_cobrar/cobro'
        context['listar_url'] = '/cuenta_cobrar/cobro/'
        return context


class CrearCuentasPdf(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template("plantillas_pdf/detalle_registros.html")
            cabecera = Cabecera.objects.all()
            pago = PagoDeuda.objects.all()
            context = {
                "titulo": "Listado de Cuentas Registradas",
                "cabecera": cabecera,
                "pagos": pago,
            }
            html = template.render(context)
            pdf = HTML(string=html).write_pdf()
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="PagosRegistrados.pdf"'
            return response
        except:
            pass
        return HttpResponseNotFound('No se ha podido encontrar el pdf')



