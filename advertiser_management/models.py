from django.db import models
from django.contrib.auth.models import User


class BaseAdvertise(models.Model):
    active = models.BooleanField(default=True)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Advertiser(BaseAdvertise):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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

    class Meta:
        verbose_name = "Advertise"


