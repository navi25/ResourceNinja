from django.db import models
from django.utils import timezone

class training(models.Model):
    trainingId=models.IntegerField()
    trainingName=models.CharField(max_length=50)
    trainingRequired=models.BooleanField()
