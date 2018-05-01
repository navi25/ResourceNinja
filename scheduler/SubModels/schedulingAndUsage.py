from django.db import models
from django.utils import timezone

class schedulingAndUsage(models.Model):
    machineStatus=models.CharField(max_length=50)
    time=models.DateTimeField()
    date=models.DateTimeField()
    laborID=models.IntegerField()
