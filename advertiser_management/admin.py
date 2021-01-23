from django.contrib import admin
from .models import *


# Register your models here.

class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ['username']

    class Meta:
        model = Advertiser


admin.site.register(Advertiser, AdvertiserAdmin)


class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Advertise


admin.site.register(Advertise, AdvertiseAdmin)
