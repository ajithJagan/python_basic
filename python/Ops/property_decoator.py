 
class call_student():
     def __init__(self,name,age):
         self.name = name
         self.age = age
         
     @property
     def view_name(self):
         return "my name is " + self.name+ " and my age is " + str(self.age) + " years old"

obj = call_student("ajith",20)

print(obj.view_name)
     
     