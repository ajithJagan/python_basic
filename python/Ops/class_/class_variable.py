
class student():
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.count += 1

    @classmethod
    def view_count(cls):
        return cls.count

obj = student("ajith",20 )
print(student.view_count())

obj = student("ajith",21 )

print(student.count)
obj = student("ajith",21 )
print(student.count)
obj = student("ajith",21 )
print(obj.count)
