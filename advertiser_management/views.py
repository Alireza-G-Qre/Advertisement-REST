from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
from .forms import AdvertiserCreationForm, AdvertiseCreationForm, LoginAdvertiserForm
from django.contrib.auth import login


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
        result = super().form_valid(form)
        Advertiser.objects.create(user=self.object)
        return result


class AdvertiseRegister(CreateView):
    model = Ad
    success_url = '/advertiserList'
    template_name = 'CreateAdvertise.html'
    form_class = AdvertiseCreationForm


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
    template_name = 'AdvertiserList.html'
