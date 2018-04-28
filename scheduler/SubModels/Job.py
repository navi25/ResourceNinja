from django.db import models

class Job(models.Model):

  def __init__(self, jobID, materialRequested, customerID, maxHeight, totalVolume, requestedDate, expedited, specialInstructions):

    self.jobID = jobID
    self.materialRequested = materialRequested
    self.customerID = customerID
    self.maxHeight = maxHeight
    self.totalVolume = totalVolume
    self.requestedDate = requestedDate
    self.expedited = expedited
    self.specialInstructions = specialInstructions

  def getJobID(self):
        return self.jobID

  def setJobID(self, x):
        if not isinstance(x, int):
            raise TypeError("Must be set to an integer")
        self.jobID = x

  def getMaterialRequested(self):
        return self.materialRequested

  def setMaterialRequested(self, x):
        if not isinstance(x, str):
            raise TypeError("Must be set to a string")
        self.materialRequested = x

  def getCustomerID(self):
        return self.customerID

  def setCustomerID(self, x):
        if not isinstance(x, int):
            raise TypeError("Must be set to an integer")
        self.customerID = x

  def getMaxHeight(self):
        return self.maxHeight

  def setMaxHeight(self, x):
        if not isinstance(x, float):
            raise TypeError("Must be set to a float")
        self.maxHeight = x

  def getTotalVolume(self):
        return self.totalVolume

  def setTotalVolume(self, x):
        if not isinstance(x, int):
            raise TypeError("Must be set to an float")
        self.totalVolume = x

  def getRequestedDate(self):
        return self.requestedDate

  def setRequestedDate(self, x):
        if not isinstance(x, str): #we need to add a datetime and currency class
            raise TypeError("Must be set to an string")
        self.requestedDate = x

  def getExpedited(self):
        return self.expedited

  def setExpedited(self, x):
        if not isinstance(x, bool):
            raise TypeError("Must be set to a boolean")
        self.expedited = x

  def getSpecialInstructions(self):
        return self.specialInstructions

  def setSpecialInstructions(self, x):
        if not isinstance(x, str):
            raise TypeError("Must be set to an string")
        self.specialInstructions = x
