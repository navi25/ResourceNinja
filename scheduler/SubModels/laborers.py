from django.db import models
from django.utils import timezone


class laborers(models.Model):
    laborId=models.IntegerField()
    name=models.CharField(max_length=50)
    trainingId=models.IntegerField()
    employeeCategory=models.CharField(max_length=50)
    employeeRate=models.CharField(max_length=50)
    benefits=models.TextField()
    cost=models.FloatField()
