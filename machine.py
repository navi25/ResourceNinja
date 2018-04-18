class Machine:

    def __init__(self, machineID, machineModelNumber, machineManufacturer, machineModelYear, machinePurchaseDate, machineCostOfPurchase, materialID, trainingID,
    machineMaintenancePeriod, machineMaintenanceDuration, maintenanceCostPerYear, consumablesCostPerHour):   

        self.machineID = machineID
        self.machineModelNumber = machineModelNumber
        self.machineManufacturer = machineManufacturer
        self.machineModelYear = machineModelYear
        self.machinePurchaseDate = machinePurchaseDate
        self.machineCostOfPurchase = machineCostOfPurchase
        self.materialID = materialID
        self.trainingID = trainingID
        self.machineMaintenancePeriod = machineMaintenancePeriod
        self.machineMaintenanceDuration = machineMaintenanceDuration
        self.maintenanceCostPerYear = maintenanceCostPerYear
        self.consumablesCostPerHour = consumablesCostPerHour


    def getMachineID(self):
        return self.machineID

    def setMachineID(self, x):
        self.machineID = x
    
    def getMachineModelNumber(self):
        return self.machineModelNumber

    def setMachineModelNumber(self, x):
        self.machineModelNumber = x

    def getMachineManufacturer(self):
        return self.machineManufacturer

    def setMachineManufacturer(self, x):
        self.machineManufacturer = x


    def getMachineModelYear(self):
        return self.machineModelYear

    def setMachineModelYear(self, x):
        self.machineModelYear = x