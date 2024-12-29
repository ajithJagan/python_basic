
class Bus():
    def __init__(self,busName): # __init__ is a constructor in python , it is used to initialize the object
        print("Bus is created")
        self.busName = busName
    def viewBusName(self):
        print(f"The bus name is {self.busName}")
        
        
o = Bus("Volvo")

o1 = Bus("Ashok Leyland")

o.viewBusName()
o1.viewBusName()

