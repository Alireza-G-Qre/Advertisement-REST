from rest_framework.routers import DefaultRouter

from .views import *
from knox import views as knox
from django.urls import path, include

app_name = 'advertise'

router = DefaultRouter()
router.register(r'advertiser', AdvertiserView, basename='advertiser')
router.register(r'ad', AdView, basename='ad')

urlpatterns = [
    path('', include(router.urls)),
    path(r'login', LoginKnoxView.as_view(), name='login'),
    path(r'logout', knox.LogoutView.as_view(), name='logout'),
]
