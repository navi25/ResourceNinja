from django.db import models

class Training(models.Model):

  def __init__(self, trainingID, trainingName, trainingRequired):

    self.trainingID = trainingID
    self.trainingName = trainingName
    self.trainingRequired = trainingRequired

  def getTrainingID(self):
        return self.trainingID

  def setTraininID(self, x):
        if not isinstance(x, int):
            raise TypeError("Must be set to integer")
        self.trainingID = x

  def getTrainingName(self):
        return self.trainingName

  def setTrainingName(self, x):
        if not isinstance(x, str):
              raise TypeError("Must be set to string")
        self.trainingName = x

  def getTrainingRequired(self):

        return self.trainingRequired

  def setTrainingRequired(self, x):
        if not isinstance(x, bool):
              raise TypeError("Must be set to boolean")
        self.trainingRequired = x
