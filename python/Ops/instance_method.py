class Car():
    name = "swift"
    model = "2024"
    color = "red"
  
    def view_car(self):  #self is a keyword in python , it is used to refer to the current instance of the class
        print(f"The car name is {Car.name} and the model is {Car.model} and the color is {Car.color}")
        
# Car.view_car()

o =Car()

o.view_car()  # this is the way to call the instance method using object

Car.view_car(o)  # this is the way to call the instance method using class

 