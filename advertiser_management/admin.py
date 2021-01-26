from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .forms import *


# Register your models here.


class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ['user']

    class Meta:
        model = Advertiser


admin.site.register(Advertiser, AdvertiserAdmin)


class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'approve']
    fields = ['title', 'link', 'image_url', 'description', 'active', 'approve']

    class Meta:
        model = Ad


admin.site.register(Ad, AdAdmin)


class RequestedAdAdmin(admin.ModelAdmin):
    list_display = ['title', 'my_actions']
    fields = ['approve']
    actions = ['accept', 'reject']

    def accept(self, request, queryset):
        self.get_queryset(request).update(approve=True)

    def reject(self, request, queryset):
        self.delete_queryset(request, queryset)

    class Meta:
        model = RequestedAd


admin.site.register(RequestedAd, RequestedAdAdmin)
