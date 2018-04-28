from django.db import models


class machineStatus(models.Model):
    def __init__(self,machineId,status,subStatus):
        self.machineId
        self.status
        self.subStatus

    def getmachineId(self):
        return self.machineId

    def setmachineId(self, x):
        if not isinstance(x, int):
             raise TypeError("Insert a Integer")
        self.machineId = x

    def getstatus(self):
        return self.status

    def setstatus(self, x):
        if not isinstance(x, int):
             raise TypeError("Insert a Integer")
        self.status = x

    def getsubStatus(self):
        return self.subStatus

    def setSubstatus(self, x):
        if not isinstance(x, int):
             raise TypeError("Insert a Integer")
        self.subStatus = x
