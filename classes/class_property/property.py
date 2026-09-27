class Person():
    species = "Human"

    def __init__(self, name):
        self.name = name


p1 = Person("Farhan")
p2 = Person("Adi")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
p1.species = "hahaha"
print(p2.species)
Person.species = "hihihi"
print(p2.species)
Person.address = "Sleman"
p1.kelas = "A2"
print(p1.kelas)
print(p1.address)