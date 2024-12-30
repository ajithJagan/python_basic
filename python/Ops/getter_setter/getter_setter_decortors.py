class student():
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def view_name(self):
        return "my name is " + self.name + " and my age is " + str(self.age) + " years old"

    @name.setter
    def name(self,name):
        self._name = name

    @age.setter
    def age(self,age):
        self._age = age

obj = student("ajith",20)

print(obj.view_name)

obj.name = "akil"
obj.age = 21

print(obj.view_name)








