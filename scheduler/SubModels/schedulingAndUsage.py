from django.db import models


class schedulingAndUsage(models.Model):
    def __init__(self,machineStatus,time,date,laborId):
        self.machineStatus
        self.time
        self.date
        self.laborId

    def getmachineStatus(self):
        return self.machineStatus

    def setmachineStatus(self, x):
        if isinstance(x,int):
            raise TypeError("Insert Integer")
        self.machineStatus = x

    def gettime(self):
        return self.time

    def settime(self, x):
       # if isinstance(x,str):
        #    raise TypeError("Insert Integer")
        self.time = x

    def getdate(self):
        return self.date

    def setdate(self, x):
       # if isinstance(x,int):
          #  raise TypeError("Insert Integer")
        self.date = x


    def getlaborId(self):
        return self.laborId

    def setlaborId(self, x):
        if isinstance(x,int):
            raise TypeError("Insert Integer")
        self.laborId = x
