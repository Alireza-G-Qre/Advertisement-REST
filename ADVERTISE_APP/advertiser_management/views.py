from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.db.models.functions import ExtractHour
from django.views.generic import RedirectView

from serializers import *
from rest_framework.generics import *

from .forms import LoginAdvertiserForm
from .models import *


# Create your views here.

class AdvertiserView(GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    serializer_class = AdvertiserSerializer
    queryset = Advertiser.objects.filter(active=True)

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def list(self, request, *args, **kwargs):
        result = super(AdvertiserView, self).list(request, *args, **kwargs)
        print(result)
        return result

    def retrieve(self, request, *args, **kwargs):
        result = super(AdvertiserView, self).retrieve(request, *args, **kwargs)
        print(result)
        return result

    class Meta:
        model = Advertiser


class AdView(GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    queryset = Ad.objects.filter(active=True)
    serializer_class = AdvertiseSerializer

    @staticmethod
    def clicks_per_hour(obj):
        return obj.clicks.annotate(hour=ExtractHour('time')).values('hour') \
            .annotate(count=Count('hour')).values('hour', 'count')

    @staticmethod
    def views_per_hour(obj):
        return obj.views.annotate(hour=ExtractHour('time')).values('hour') \
            .annotate(count=Count('hour'))

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def list(self, request, *args, **kwargs):
        result = super(AdView, self).list(request, *args, **kwargs)
        print(result)
        return result

    def retrieve(self, request, *args, **kwargs):
        result = super(AdView, self).retrieve(request, *args, **kwargs)
        print(result)
        return result

    class Meta:
        model = Ad


class LoginAdvertiser(LoginView):
    form_class = LoginAdvertiserForm
    template_name = 'LoginAdvertiser.html'
    success_url = '/advertiserList'

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())
        if remember_me:
            self.request.session.set_expiry(1209600)

        return super(LoginAdvertiser, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginAdvertiser, self).form_invalid(form)


class LogoutAdvertiser(LogoutView):
    template_name = 'Lists/AdvertiserList.html'


class ClickRedirect(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        ad = Ad.get_by_id(kwargs['pk'])
        ad.click(self.request.ip)
        return ad.link
