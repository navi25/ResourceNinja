from django.db import models
from django.utils import timezone

class formDetails(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    comments=models.TextField()
    equipName=models.CharField(max_length=50)
    date=models.DateTimeField()
    time=models.DateTimeField()
    acctNo=models.IntegerField()
    maxHeight=models.FloatField()
    minHeight=models.FloatField()
    maxLength=models.FloatField()
    minLength=models.FloatField()
    maxWidth=models.FloatField()
    minWidth=models.FloatField()
    volume=models.FloatField()
