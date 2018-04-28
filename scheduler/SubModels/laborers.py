from django.db import models


class laborers(models.Model):
        def __init__(self,laborId,name,trainingId,employeeCategory,employeeRate,benefits,cost):
                self.laborId = laborId
                self.name=name
                self.trainingId=trainingId
                self.employeeCategory=employeeCategory
                self.employeeRate=employeeRate
                self.benefits=benefits
                self.cost=cost

        def getlaborId(self):
                return self.laborId

        def setlaborId(self, x):
                if not isinstance(x, int):
                        raise TypeError("Must be set to integer")
                self.laborId = x

        def gettraingId(self):
                return self.trainingId

        def settraingId(self, x):
                if not isinstance(x, int):
                        raise TypeError("Must be set to integer")
                self.laborId = x

        def getname(self):
                return self.name

        def setname(self, x):
                if not isinstance(x, str):
                        raise TypeError("Must be set to String")
                self.name = x

        def getemployeeCategory(self):
                return self.employeeCategory

        def setemployeeCategory(self, x):
                if not isinstance(x, str):
                        raise TypeError("Must be set to String")
                self.employeeCategory = x


        def getemployeeRate(self):
                return self.employeeRate

        def setemployeeRate(self, x):
                if not isinstance(x, float):
                        raise TypeError("Must be set to Float")
                self.employeeRate = x

        def getbenefits(self):
                return self.benefits

        def setbenefits(self, x):
                if not isinstance(x, str):
                        raise TypeError("Must be set to String")
                self.benefits = x

        def getcost(self):
                return self.cost

        def setcost(self, x):
                if not isinstance(x, float):
                        raise TypeError("Must be set to Float")
                self.cost = x
