class A:
    def view(self):
         self.name = "Ajith"
         
    def view_name(self):
         print(self.name)

class B(A):
    def view(self):
         self.name = "Jagan"

obj = A()
obj.view()
obj.view_name()


