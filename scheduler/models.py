from django.db import models
from django.urls import reverse

# Create your models here.
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


