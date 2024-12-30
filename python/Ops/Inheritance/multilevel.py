class Grandfather:
    def house(self):
        return "2BHK"

class Father(Grandfather):
    def car(self):
        return "BMW"

class Child(Father):
    def bike(self):
        return "Honda"

obj = Child()
print(obj.house())
print(obj.car())
print(obj.bike())
