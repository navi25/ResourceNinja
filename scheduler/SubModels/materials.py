from django.db import models
from django.utils import timezone

class materials(models.Model):
    materialID=models.IntegerField()
    materialName=models.CharField(max_length=50)
    formFactor=models.CharField(max_length=50)
    costPerUnit=models.FloatField()
    leadTime=models.DateTimeField()
    vendor=models.CharField(max_length=50)
    machine=models.CharField(max_length=50)
    amountOnHand=models.FloatField()
    redBinAmount=models.FloatField()
