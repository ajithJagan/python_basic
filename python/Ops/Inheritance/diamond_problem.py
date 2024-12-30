class A:
    def display(self):
        print("It is class A")
    def view(self):
        print("It is class A")
      
    
class B(A):
    def display(self):
        print("It is class B")    
        
class C(A):
    def display(self):
        print("It is class C")
class D(B,C):
    def display(self):
        print("It is class D")
        

d_obj = D()

d_obj.display()
d_obj.view()