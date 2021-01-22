from django.db import models


class BaseAdvertiseManager(models.Manager):

    def get_active_ones(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self, this_id):
        return self.get_queryset().filter(id=this_id).first()


class BaseAdvertise(models.Model):
    clicks = models.IntegerField()
    views = models.IntegerField()
    active = models.BooleanField(default=True)
    objects = BaseAdvertiseManager()


class Advertiser(BaseAdvertise):
    username = models.CharField()


class Advertise(BaseAdvertise):
    title = models.CharField()
    image_url = models.URLField()
    link = models.URLField()
    description = models.TextField()
