from django.contrib import admin
from .forms import *


# Register your models here.


class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ['user']

    class Meta:
        model = Advertiser


admin.site.register(Advertiser, AdvertiserAdmin)


class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'approve']
    fields = ['title', 'linkUrl', 'img_Url', 'description', 'active', 'approve']
    list_filter = ['approve']

    class Meta:
        model = Ad


admin.site.register(Ad, AdAdmin)
