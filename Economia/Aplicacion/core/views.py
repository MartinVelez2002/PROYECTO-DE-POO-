from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class InicioTemplateView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Menu Principal"
        context['url_anterior']= '/'
        return context