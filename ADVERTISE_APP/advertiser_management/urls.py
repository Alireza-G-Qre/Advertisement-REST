from django.urls import path
from .views import *

app_name = 'advertise'

urlpatterns = [
    path('advertiser/login', LoginAdvertiser.as_view(), name='login'),
    path('advertiser/logout', LogoutAdvertiser.as_view(), name='logout'),

    path('advertiser/newOne', CreateAdvertiser.as_view(), name='advertiser-register'),
    path('advertiser/<pk>', AdvertiserView.as_view(), name='advertiser-detail'),
    path('advertiserList', AdvertiserView.as_view(), name='advertiser-list'),

    path('advertise/<pk>', AdView.as_view(), name='ad-detail'),
    path('advertise/create', CreateAd.as_view(), name='ad-create'),
    path('advertise/<pk>', ClickRedirect.as_view(), name='ad-redirect'),
]
