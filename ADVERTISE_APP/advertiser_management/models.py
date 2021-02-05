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
        return self.ads.filter(active=True, approve=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Advertiser"
        ordering = ['id']


class Ad(BaseAdvertise):
    approve = models.BooleanField(default=False)
    title = models.CharField(max_length=30)
    link = models.URLField(max_length=2000)
    image_url = models.URLField(max_length=2000)
    description = models.TextField()

    advertiser = models.ForeignKey(
        Advertiser, on_delete=models.CASCADE, related_name='ads'
    )

    @classmethod
    def get_by_id(cls, ad_id):
        return cls.objects.get(active=True, approve=True, id=ad_id)

    def view(self, ip):
        ViewAd.objects.create(ip=ip, ad=self)

    def click(self, ip):
        ClickAd.objects.create(ip=ip, ad=self)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Advertise"


class RequestedAdManager(models.Manager):

    def get_queryset(self):
        return super(RequestedAdManager, self).get_queryset().filter(approve=False)


class RequestedAd(Ad):
    objects = RequestedAdManager()

    class Meta:
        verbose_name = "Requested Ad"
        proxy = True


class BaseVisiting(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    class Meta:
        abstract = True


class ViewAd(BaseVisiting):
    ad = models.ForeignKey(
        Ad, on_delete=models.CASCADE, related_name='views'
    )

    class Meta:
        verbose_name = "Ad View"


class ClickAd(BaseVisiting):
    ad = models.ForeignKey(
        Ad, on_delete=models.CASCADE, related_name='clicks'
    )

    class Meta:
        verbose_name = "Ad Click"
