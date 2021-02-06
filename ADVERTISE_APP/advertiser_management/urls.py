from rest_framework.routers import DefaultRouter

from .views import *
from django.urls import path, include

app_name = 'advertise'

router = DefaultRouter()
router.register(r'advertiser', AdvertiserView, basename='advertiser')
router.register(r'ad', AdView, basename='ad')

urlpatterns = [
    path('', include(router.urls)),
    path(r'login', LoginAPIView.as_view(), name='login'),
    path(r'logout', LogoutAPIView.as_view(), name='logout'),
]
