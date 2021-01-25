from django.db import models
from django.contrib.auth.models import User


class BaseAdvertise(models.Model):
    active = models.BooleanField(default=True)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

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

    def view(self):
        self.views += 1
        self.save()

    def click(self):
        self.clicks += 1
        self.save()


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

    class Meta:
        verbose_name = "Advertise"

    def view(self):
        self.views += 1
        self.advertiser.view()
        self.save()

    def click(self):
        self.clicks += 1
        self.advertiser.click()
        self.save()
