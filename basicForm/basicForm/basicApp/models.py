from django.db import models

# Create your models here.
class Machine:
    class Meta:
        def __init__(self, _id, _name, _manufacturer, _material):
            self.id = _id
            self.name = _name
            self.manufacturer = _manufacturer
            self.material = _material

class Material:
    class Meta:
        def __init__(self, _id, _name, _vendor):
            self.id = _id
            self.name = _name
            self.vendor = _vendor

