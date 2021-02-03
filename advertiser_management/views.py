from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, RedirectView, FormView
from .models import *
from .forms import AdvertiserCreationForm, AdvertiseCreationForm, LoginAdvertiserForm
from django.contrib.auth import login


# Create your views here.

class AdvertiserList(ListView):
    model = Advertiser
    template_name = 'Lists/AdvertiserList.html'
    paginate_by = 4
    context_object_name = 'advertisers'

    def get_queryset(self):

        advertisers = Advertiser.objects.filter(active=True)

        for advertiser in advertisers:

            ads = advertiser.get_ads()
            _limit = min(len(ads), self.paginate_by)
            for number in range(_limit):
                ads[number].view(self.request.ip)

        return advertisers


class AdvertiserRegister(CreateView):
    model = User
    success_url = '/advertiserList'
    template_name = 'CreateAdvertiser.html'
    form_class = AdvertiserCreationForm

    def form_valid(self, form):
        result = super().form_valid(form)
        Advertiser.objects.create(user=self.object)
        return result


class AdvertiseRegister(CreateView):
    model = Ad
    success_url = '/advertiserList'
    template_name = 'CreateAdvertise.html'
    form_class = AdvertiseCreationForm

    def form_valid(self, form):
        form.instance.advertiser = self.request.user.advertiser
        return super().form_valid(form)


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


class AdvertiserDetailView(DetailView):
    template_name = 'Lists/AdvertiseList.html'
    model = Advertiser
    context_object_name = 'advertiser'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        ads = result['advertiser'].get_ads()
        for ad in ads:
            ad.view(self.request.ip)

        return result


class ClickRedirect(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        ad = Ad.get_by_id(kwargs['pk'])
        ad.click(self.request.ip)
        return ad.link


class AdDetailView(DetailView):
    template_name = 'AdvertiseDetail.html'
    model = Ad
    context_object_name = 'ad'

    @staticmethod
    def clicks_per_hour(obj):
        return obj.clicks.annotate(hour=ExtractHour('time')).values('hour') \
            .annotate(count=Count('hour')).values('hour', 'count')

    @staticmethod
    def views_per_hour(obj):
        return obj.views.annotate(hour=ExtractHour('time')).values('hour') \
            .annotate(count=Count('hour'))

    def get_context_data(self, **kwargs):
        data = super(AdDetailView, self).get_context_data(**kwargs)
        data['clicks_per_hour'] = self.clicks_per_hour(data['ad'])
        data['views_per_hour'] = self.views_per_hour(data['ad'])
        return data
