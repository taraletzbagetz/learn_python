class MyClass:
    x = 5

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def _str_(self):
        return f"{self.name}({self.age})"


p1 = MyClass()
print(p1.x)

p2 = Person("John", 36)

print(p2.name)
print(p2.age)
print(p2)

