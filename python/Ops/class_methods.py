
class Car():
    name = "swift"
    model = "2024"
    color = "red"
  
    def view_car():
        print(f"The car name is {Car.name} and the model is {Car.model} and the color is {Car.color}")
        
Car.view_car()  # this is the way to call the class method using class

# o =Car()

# o.view_car()  # this is the way to call the class method using object , but we can't call the class method using object ,why because it is not a instance method

 
