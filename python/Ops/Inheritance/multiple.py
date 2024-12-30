class Father:
    father_age = 50
    def father_name(self):
        return "Jagan"

class Mother:
    mother_age = 45
    def mother_name(self):
        return "Selvi"

class Child(Father,Mother):
    child_age = 20
    def child_name(self):
        return "Ajith"


obj = Child()
print(obj.father_name())
print(obj.mother_name())
print(obj.child_name())
print(obj.father_age)
print(obj.mother_age)
print(obj.child_age)

