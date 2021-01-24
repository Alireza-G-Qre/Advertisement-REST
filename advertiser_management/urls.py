from django.urls import path
from .views import *

app_name = 'advertise'

urlpatterns = [
    path('advertiser/login', LoginAdvertiser.as_view(), name='login'),
    path('advertiser/logout', LogoutAdvertiser.as_view(), name='logout'),
    path('advertiserList', AdvertiserList.as_view(), name='list'),
    path('advertiser/new', AdvertiserRegister.as_view(), name='register'),
    path('advertise/new', AdvertiseRegister.as_view(), name='create_ad'),
]
