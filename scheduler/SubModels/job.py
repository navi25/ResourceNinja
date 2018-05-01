from django.db import models
from django.utils import timezone

class job(models.Model):
    jobID=models.IntegerField()
    materialRequested=models.CharField(max_length=50)
    customerID=models.IntegerField()
    maxHeight=models.FloatField()
    requestedDate=models.DateTimeField
    expedited= models.BooleanField
    specialInstruction=models.TextField()
