from celery import shared_task
from .models import ClickAd, ViewAd, Report
from datetime import datetime, timedelta


@shared_task()
def analysis_every_hour():
    now = datetime.now()
    clicks = ClickAd.objects.filter(date__gt=now - timedelta(hours=1))
    views = ViewAd.objects.filter(date__gt=now - timedelta(hours=1))
    Report.objects.create(type='every hour', time=now, number_of_clicks=clicks, number_of_views=views)


@shared_task()
def analysis_every_day():
    now = datetime.now()
    clicks = ClickAd.objects.filter(date__gt=now - timedelta(days=1))
    views = ViewAd.objects.filter(date__gt=now - timedelta(days=1))
    Report.objects.create(type='every day', time=now, number_of_clicks=clicks, number_of_views=views)
