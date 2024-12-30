
class Car():
   def __init__(self,name,model,color):
       self.name = name
       self.model = model
       self.color = color
       
   def view_car(self):
       print(f"The car name is {self.name} and the model is {self.model} and the color is {self.color}")

   @staticmethod
   def welcome():
       print("Welocome buddy to the car world")

o = Car("swift","2024","red")
o.view_car()
o.welcome()


