from django.db import models
from django.contrib.auth.models import User


class BaseAdvertise(models.Model):
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Advertiser(BaseAdvertise):
    user = models.OneToOneField(User, related_name='advertiser', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Advertiser"
        ordering = ['id']


class Ad(BaseAdvertise):
    advertiser = models.ForeignKey(Advertiser, related_name='ads', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    approve = models.BooleanField(default=False)
    linkUrl = models.URLField(max_length=2000)
    img_Url = models.URLField(max_length=2000)
    description = models.TextField()

    class Meta:
        verbose_name = "Advertise"


class BaseVisiting(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    class Meta:
        abstract = True


class ViewAd(BaseVisiting):
    ad = models.ForeignKey(Ad, related_name='views', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ad View"


class ClickAd(BaseVisiting):
    ad = models.ForeignKey(Ad, related_name='clicks', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ad Click"
