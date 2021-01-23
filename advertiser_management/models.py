from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseAdvertise(models.Model):
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    active = models.BooleanField(default=True)


class Advertiser(AbstractUser, BaseAdvertise):

    def get_advertises(self):
        return Advertise.objects.get_by_advertiser(self.id)

    class Meta:
        verbose_name = "Advertiser"


class AdvertiseManager(models.Manager):

    def get_active_ones(self):
        return self.get_queryset().filter(active=True)

    def get_by_advertiser(self, advertiser):
        return self.get_active_ones().filter(advertiser_id=advertiser)


class Advertise(BaseAdvertise):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    link = models.URLField()
    advertiser_id = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    description = models.TextField()
    objects = AdvertiseManager()
