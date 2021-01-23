from django.urls import path
from .views import *

app_name = 'advertise'

urlpatterns = [
    path('advertiserList', AdvertiserList.as_view(), name='advertiserList'),
    path('advertiser/new', AdvertiserRegister.as_view(), name='advertiser_new'),
    path('advertise/new', AdvertiseRegister.as_view(), name='advertise_new'),
]
