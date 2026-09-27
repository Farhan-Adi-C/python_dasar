class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
    def __str__(self):
        return f"ini adalah {self.name}"

p1 = Person("Farhan", 20)
print(repr(p1))