from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class AdvertiserAdmin(UserAdmin):
    model = Advertiser
    add_form = AdvertiserCreationForm
    form = AdvertiserChangeForm
    list_display = ['username', 'clicks', 'views']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ['clicks', 'views']}),)


admin.site.register(Advertiser, AdvertiserAdmin)


class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Advertise


admin.site.register(Advertise, AdvertiseAdmin)
