from django.views.generic import TemplateView, RedirectView
from django.shortcuts import render


class BehindHeader(TemplateView):
    template_name = 'shared/_Header.html'

    def post(self, request, **kwargs):
        return render(request, self.template_name)


class BehindFooter(TemplateView):
    template_name = 'shared/_Footer.html'

    def post(self, request, **kwargs):
        return render(request, self.template_name)


class Home(RedirectView):
    url = '/advertiserList'
