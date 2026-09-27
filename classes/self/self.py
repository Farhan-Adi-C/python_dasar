class Person() :
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print("Hello " + self.name + " Welcome to tutorial")

    def welcome(self):
       self.greeting()
       print("wkwkwk")

person1 = Person("farhan")
person1.welcome()


class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()