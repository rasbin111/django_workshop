import os
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# For scheduling task - method 2
app.conf.beat_schedule = {
    "every-10-seconds": {  # can name anything every-10-seconds, ets, etens, ess
        "task": "course.tasks.clear_session_cache",
        # "schedule": 10,
        "schedule": timedelta(seconds=10),
        # "schedule": crontab(minute="*/1"),
        "args": ("1111111", )
    }
}