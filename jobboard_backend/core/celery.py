from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from decouple import config

# Set default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Namespace 'CELERY_' prefixes all related config keys in settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Using Redis as the message broker
app.conf.broker_url = config('REDIS_URL')

# Auto-discover tasks in all Django app configs
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
