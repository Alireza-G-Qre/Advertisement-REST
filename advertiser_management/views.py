from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import *
from .forms import RegisterAdvertiser


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


class AdvertiserRegister(CreateView):
    model = Advertiser
    fields = ['username', 'password', 'email']
    success_url = 'advertiserList'
    form_class = RegisterAdvertiser





