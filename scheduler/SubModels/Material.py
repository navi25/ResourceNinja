from django.db import models

class Material(models.Model):

  def __init__(self, materialID, materialName, formFactor, costPerUnit, leadTime, vendor, machine, amountOnHand, redBinAmount):

    self.materialID = materialID
    self.materialName = materialName
    self.formFactor = formFactor
    self.costPerUnit = costPerUnit
    self.leadTime = leadTime
    self.vendor = vendor
    self.machine = machine
    self.amountOnHand = amountOnHand
    self.redBinAmount = redBinAmount

  def getMaterialID(self):
        return self.materialID

  def setMaterialID(self, x):
        if not isinstance(x, int):
            raise TypeError("Must be set to an integer")
        self.materialID = x

  def getMaterialName(self):
        return self.materialName

  def setMaterialName(self, x):
        if not isinstance(x, str):
            raise TypeError("Must be set to a string")
        self.materialName = x

  def getFormFactor(self):
        return self.formFactor

  def setFormFactor(self, x):
        if not isinstance(x, str):
            raise TypeError("Must be set to a string")
        self.formFactor = x

  def getCostPerUnit(self):
        return self.costPerUnit

  def setCostPerUnit(self, x):
        if not isinstance(x, float):
            raise TypeError("Must be set to a float")
        self.costPerUnit = x

  def getLeadTime(self):
        return self.leadTime

  def setLeadTime(self, x):
        if not isinstance(x, int):
            raise TypeError("Must be set to an integer")
        self.leadTime = x

  def getVendor(self):
        return self.vendor

  def setVendor(self, x):
        if not isinstance(x, str):
            raise TypeError("Must be set to a string")
        self.vendor = x

  def getMachine(self):
        return self.machine

  def setMachine(self, x):
        if not isinstance(x, str):
            raise TypeError("Must be set to a str")
        self.machine = x

  def getAmountOnHand(self):
        return self.amountOnHand

  def setAmountOnHand(self, x):
        if not isinstance(x, float):
            raise TypeError("Must be set to a float")
        self.amountOnHand = x

  def getRedBinAmount(self):
        return self.redBinAmount

  def setRedBinAmount(self, x):
        if not isinstance(x, float):
            raise TypeError("Must be set to a float")
        self.redBinAmount = x
