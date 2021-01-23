from django.views.generic.list import ListView
from .models import *


# Create your views here.


class AdvertiseList(ListView):
    model = Advertise
    template_name = ''
    paginate_by = 4

    def get_queryset(self):
        return Advertise.objects.get_active_ones()


class AdvertiserList(ListView):
    model = Advertiser
    template_name = 'AdvertiserList.html'
    paginate_by = 4
    context_object_name = 'advertisers'

    def get_queryset(self):
        return Advertiser.objects.get_active_ones()

