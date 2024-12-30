class student():
    def __init__(self,name):
        self._name = name

    def getter(self):
        return self._name
    
    def setter(self,name):
        self._name = name


    @property
    def view_name(self):
        return "my name is " + self.name 

    name = property(getter,setter)

obj = student("ajith")

print(obj.view_name)

obj.name = "akil"

print(obj.view_name)








