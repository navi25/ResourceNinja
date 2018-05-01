from django.db import models

class machineStatus(models.Model):
    machineID=models.IntegerField()
    status=models.CharField(max_length=50)
    subStatus=models.CharField(max_length=50)
    
