class Makanan():
    def __init__(self, name, price):
        self.name = name
        self.price = str(price)
    def info(self):
        print("the price of the  " + self.name + " menu is " + self.price)


menu1 = Makanan("Soto", 5000)
menu1.info()

class Calculator():
    def add(self, a, b):
        return a + b

    def multipy(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(2, 3))
print(calc.multipy(2, 3))

class Student():
    grade = 90
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check(self):
        self.grade += 10
        print(f"{self.name}'s Scores is {self.grade} ")    

    def __str__(self):
        return "Ini adalah siswa yang bernama " + self.name

st1 = Student("Farhan", 17)
st1.check()
st1.check()

print(st1)