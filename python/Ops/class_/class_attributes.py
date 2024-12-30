
class Ajith():
    name = "ajith"
    age =12

print(getattr(Ajith,'name'))

print(getattr(Ajith,'age'))


print(Ajith.name)

print(Ajith.age)

print(setattr(Ajith,'name','akil'))
print(Ajith.name)


# print(Ajith.name)

Ajith.ooru='salem'

print(Ajith.ooru)
print(Ajith.__dict__)
delattr(Ajith,'name')
del Ajith.age
print(Ajith.__dict__)


