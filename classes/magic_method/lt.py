class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __lt__(self, other):
    return self.age > other.age

p1 = Person("Emil", 22)
p2 = Person("Tobias", 19)
p3 = Person("Farhan", 10)

print(p1 < p2)
x = sorted([p1, p2, p3])
print(x[0].age)
