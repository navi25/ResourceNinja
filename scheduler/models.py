from django.db import models
from django.urls import reverse

# Create your models here.

from scheduler.SubModels import laborers
from scheduler.SubModels import formDetails
from scheduler.SubModels import materials
from scheduler.SubModels import job
from scheduler.SubModels import training
from scheduler.SubModels import machine
from scheduler.SubModels import customers
from scheduler.SubModels import machineStatus
from scheduler.SubModels import schedulingAndUsage
class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customers')

    def get_individual_url(self):
        return reverse('customer-detail',args=[str(self.id)])


class MachineModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('machines')


class OrderModel(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateSubmitted = models.DateField()
    datePartsNeeded =  models.DateField()
    facultyAdvisor = models.CharField(max_length=200)
    paymentAccountNo = models.IntegerField()
    className = models.CharField(max_length=100)
    machineRequested = models.CharField(max_length=200)
    listParts = models.CharField(max_length=200)
    maxHeight=models.FloatField(default=None)
    minHeight=models.FloatField(default=None)
    maxLength=models.FloatField(default=None)
    minLength=models.FloatField(default=None)
    maxWidth=models.FloatField(default=None)
    minWidth=models.FloatField(default=None)
