from django.db.models.functions import ExtractHour
from django.views.generic import RedirectView
from django.db.models import Count

from advertiser_management.serializers import *
from rest_framework.viewsets import *
from knox import views as knox
from .models import *


# Create your views here.

class AdvertiserView(ModelViewSet):
    queryset = Advertiser.objects.filter(active=True)
    serializer_class = AdvertiserSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    class Meta:
        model = Advertiser


class AdView(ModelViewSet):
    queryset = Ad.objects.filter(active=True, approve=True)
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

    def retrieve(self, request, *args, **kwargs):
        result = super(AdView, self).retrieve(request, *args, **kwargs)
        result.data['clicks_per_hour'] = self.clicks_per_hour(self.get_object())
        result.data['views_per_hour'] = self.views_per_hour(self.get_object())
        return result

    def create(self, request, *args, **kwargs):
        request.data['advertiser'] = request.user.advertiser
        return super(AdView, self).create(request, *args, **kwargs)

    class Meta:
        model = Ad


class LoginKnoxView(knox.LoginView):
    parser_classes = LoginSerializer

class ClickRedirect(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        ad = Ad.objects.get(id=kwargs['pk'])
        ad.click(self.request.ip)
        return ad.link
