from django.db import models
from django.contrib.auth.models import User


class BaseAdvertise(models.Model):
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Advertiser(BaseAdvertise):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='advertiser'
    )

    def get_ads(self):
        return self.ads.filter(active=True)

    class Meta:
        verbose_name = "Advertiser"
        ordering = ['id']


class Ad(BaseAdvertise):
    title = models.CharField(max_length=30)
    link = models.URLField(max_length=2000)
    image_url = models.URLField(max_length=2000)
    description = models.TextField()

    advertiser = models.ForeignKey(
        Advertiser, on_delete=models.CASCADE, related_name='ads'
    )

    @classmethod
    def get_by_id(cls, ad_id):
        return cls.objects.get(active=True, id=ad_id)

    def view(self, ip):
        View_Ad.objects.create(ip=ip, ad=self)

    def click(self, ip):
        Click_Ad.objects.create(ip=ip, ad=self)

    class Meta:
        verbose_name = "Advertise"


class BaseVisiting(models.Model):
    time = models.DateTimeField(auto_now=True)
    ip = models.GenericIPAddressField()

    class Meta:
        abstract = True


class View_Ad(BaseVisiting):
    ad = models.ForeignKey(
        Ad, on_delete=models.CASCADE, related_name='views'
    )

    class Meta:
        verbose_name = "Ad View"
        ordering = ['-id']


class Click_Ad(BaseVisiting):
    ad = models.ForeignKey(
        Ad, on_delete=models.CASCADE, related_name='clicks'
    )

    class Meta:
        verbose_name = "Ad Click"
        ordering = ['-id']
