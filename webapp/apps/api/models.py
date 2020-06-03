from django.db import models
from mew.core.models import BaseModel
from simple_history.models import HistoricalRecords

from datetime import datetime


class Facility(BaseModel):
    """
    """
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(max_length=255)
    longitude = models.FloatField(max_length=255)


class Parking(BaseModel):
    """
    """
    facility_id = models.IntegerField(default=0)
    vehicle_type = models.CharField(max_length=255, default='')
    total_slots = models.IntegerField(default=0)
    available_slots = models.IntegerField(default=0)


class Ticket(BaseModel):
    """
    """
    facility_id = models.IntegerField(default=0)
    vehicle_type = models.CharField(max_length=255, default='')
    start_time = models.DateTimeField(default=datetime.strptime("31/12/9999 23:59:59", "%d/%m/%Y %H:%M:%S"))
    end_time = models.DateTimeField(null=True)
    amount = models.FloatField()
    reg_no = models.CharField(max_length=255, default='')
