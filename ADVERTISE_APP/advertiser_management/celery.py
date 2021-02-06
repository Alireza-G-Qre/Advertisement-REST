import os
from celery import Celery, schedules

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ADVERTISE_APP.settings')
app = Celery('advertisement_management')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add-every-1-hour': {
        'task': 'tasks.analysis_every_hour',
        'schedule': schedules.crontab(minute=0),
        'args': ()
    },
    'add-every-1-day': {
        'task': 'tasks.analysis_every_day',
        'schedule': schedules.crontab(hour=0),
        'args': ()
    },
}
app.conf.timezone = 'UTC'
app.autodiscover_tasks()
