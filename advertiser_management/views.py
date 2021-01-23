from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import *
from .forms import AdvertiserCreationForm


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
        return Advertiser.objects.filter(active=True)


class AdvertiserRegister(CreateView):
    model = Advertiser
    success_url = 'advertiserList'
    template_name = 'CreateAdvertiser.html'
    form_class = AdvertiserCreationForm

    def form_valid(self, form):
        print(form.cleaned_data['username'])
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_invalid(form)
