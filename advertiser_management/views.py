from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import *
from .forms import AdvertiserCreationForm, AdvertiseCreationForm


# Create your views here.

class AdvertiserList(ListView):
    model = Advertiser
    template_name = 'AdvertiserList.html'
    paginate_by = 4
    context_object_name = 'advertisers'

    def get_queryset(self):
        return Advertiser.objects.filter(active=True)


class AdvertiserRegister(CreateView):
    model = User
    success_url = '/advertiserList'
    template_name = 'CreateAdvertiser.html'
    form_class = AdvertiserCreationForm

    def form_valid(self, form):
        Advertiser.objects.create(user=self.object)
        return super().form_valid(form)


class AdvertiseRegister(CreateView):
    model = Ad
    success_url = '/advertiserList'
    template_name = 'CreateAdvertise.html'
    form_class = AdvertiseCreationForm
