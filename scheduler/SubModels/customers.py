from django.db import models

class customers(models.Model):
        def __init__(self,customerId,company,personOfContact,email,phone):
            self.customerId
            self.company
            self.personOfContact
            self.email
            self.phone

        def getcustomerId(self):
            return self.customerId

        def setcustomerId(self, x):
          if not isinstance(x, int):
            raise TypeError("Insert a Integer")
          self. customerId = x

        def getcompany(self):
            return self.company

        def setcompany(self, x):
            if not isinstance(x, str):
                raise TypeError("Insert a String")
            self.company =x

        def getpersonOfContact(self):
             return self.personOfContact

        def setpersonOfContact(self, x):
            if not isinstance(x, str):
                raise TypeError("Insert a String")
            self.personOfContact = x

        def getemail(self):
            return self.email

        def setemail(self, x):
            if not isinstance(x, str):
                raise TypeError("Insert a String")
            self.email =x

        def getphone(self):
            return self.phone

        def setphone(self, x):
            if not isinstance(x, int):
                raise TypeError("Insert a Integer")
            self.phone = x
