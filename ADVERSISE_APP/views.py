from django.views.generic import TemplateView


class BehindHeader(TemplateView):
    template_name = 'shared/_Header.html'


class BehindFooter(TemplateView):
    template_name = 'shared/_Footer.html'
