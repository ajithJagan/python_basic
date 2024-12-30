class Bmw :
    def __init__(self):
        self.name = "BMW"
        self.founder = "Karl Rapp"
        self.year = 1916

    def view_bmw(self):
        print(f"The car name is {self.name} and the founder is {self.founder} and the year is {self.year}")

class M_series(Bmw):
    
    # view_founder =""
    
    def __init__(self):
        self.model = "M-series"
        self.color = "Black"
        self.price = 100000
        super().__init__()
        self.view_founder = self.founder

    def view_car(self):
        print(f"The car name is {self.name} and the model is {self.model} and the color is {self.color} and the price is {self.price} and the founder is {self.founder} and the year is {self.year}")
        
    def view_founder(self):
        print(f"The founder is {self.view_founder}")

obj = M_series()
# obj.view_bmw()
# obj.view_car()

print(obj.model)    

obj.view_founder()
