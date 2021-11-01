from django.views.generic.base import TemplateView


class AppView(TemplateView):
    template_name = 'app2/index.html'
