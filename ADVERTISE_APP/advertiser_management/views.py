from django.contrib.auth import login, logout
from django.db.models.functions import ExtractHour
from django.views.generic import RedirectView
from django.db.models import Count
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from advertiser_management.serializers import *
from rest_framework.viewsets import *
from rest_framework.generics import *
from .models import *


# Create your views here.
from .permissions import IsAdvertiser, NotAuthentication


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

    class Meta:
        model = Ad


class LoginAPIView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [NotAuthentication]

    @staticmethod
    def post(request):
        user = get_object_or_404(
            User,
            username=request.data['username'],
            password=request.data['password'],
        )
        token, created = Token.objects.get_or_create(user=user)
        login(request, token.user)
        return Response(data={'auth_token': token.key}, status=HTTP_200_OK)


class LogoutAPIView(GenericAPIView):

    @staticmethod
    def get(request):
        logout(request)
        return Response(status=HTTP_200_OK)


class ClickRedirect(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        ad = Ad.objects.get(id=kwargs['pk'])
        ad.click(self.request.ip)
        return ad.link
