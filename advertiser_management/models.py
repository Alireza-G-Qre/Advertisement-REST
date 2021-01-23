from django.db import models


class BaseAdvertise(models.Model):
    clicks = models.IntegerField()
    views = models.IntegerField()
    active = models.BooleanField(default=True)


class BaseAdvertiseManager(models.Manager):

    def get_active_ones(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self, this_id):
        return self.get_active_ones().filter(id=this_id).first()


class Advertiser(BaseAdvertise):
    username = models.CharField(max_length=30)
    email = models.EmailField(default='Google@gmail.com')
    objects = BaseAdvertiseManager()

    def get_advertises(self):
        return Advertise.objects.get_by_advertiser(self.id)


class AdvertiseManager(BaseAdvertiseManager):

    def get_by_advertiser(self, advertiser):
        return self.get_active_ones().filter(advertiser_id=advertiser)


class Advertise(BaseAdvertise):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    link = models.URLField()
    advertiser_id = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    description = models.TextField()
    objects = AdvertiseManager()
