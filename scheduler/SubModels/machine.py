from django.db import models
from django.utils import timezone

class machine(models.Model):
    machineID=models.IntegerField()
    machineModelNumber=models.IntegerField()
    machineModelNumber=models.CharField(max_length=50)
    machineModelYear=models.DateTimeField()
    machinePurchaseDate=models.DateTimeField()
    machineCostOfPurchase=models.FloatField()
    materialID=models.IntegerField()
    trainingID=models.IntegerField()
    machineMaintenancePeriod=models.IntegerField()
    machineMaintenanceDuration=models.IntegerField()
    maintenanceCostPerYear=models.FloatField()
    consumablesCostPerHour=models.FloatField()
    machineName=models.CharField(max_length=100, default="")
