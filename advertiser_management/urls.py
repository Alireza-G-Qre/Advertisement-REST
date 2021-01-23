from django.urls import path
from .views import *

app_name = 'advertise'

urlpatterns = [
    path('advertiserList', AdvertiserList.as_view()),
    path('Advertiser/new', AdvertiserRegister.as_view(), name='advertiser_new'),
]
