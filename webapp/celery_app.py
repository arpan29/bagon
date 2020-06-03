from __future__ import absolute_import

import logging
import os
import json

from datetime import datetime

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.conf.settings')

app = Celery('webapp')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

logger = logging.getLogger('default')


@app.task(bind=True)
def my_queue_processor(self, params):

    logger.info("Received Task: " + json.dumps(params))
    pass
