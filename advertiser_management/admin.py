from django.contrib import admin
from .forms import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class AdvertiserAdmin(UserAdmin):
    list_display = ['username', 'clicks', 'views']

    class Meta:
        model = Advertiser


admin.site.register(Advertiser, AdvertiserAdmin)


class AdAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Ad


admin.site.register(Ad, AdAdmin)
