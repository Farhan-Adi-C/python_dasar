class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Farhan", 20)

print(person1.age)
person1.age = 30
print(person1.age)

print(person1.name)
del person1.name