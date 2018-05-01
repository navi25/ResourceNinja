from django.db import models

class customers(models.Model):
    customerID=models.IntegerField()
    company=models.CharField(max_length=50)
    personOfContact=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    
