
class study():
    name = "ajith"
    age = 12

obj = study()

print(obj.__dict__)

obj.name = "akil"
print(obj.__dict__)

print(obj.name)
print(obj.age)

