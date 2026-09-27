# class Person():
#     def __init__(self, name, nik):
#         self.name = name
#         self.__nik = nik
#     def callNik(self):
#         return self.__nik
#     def changeNik(self, nik):
#         if(nik > 0):
#             self.__nik = nik
#         else:
#             print("nik must be valid")

# p1 = Person("Farhan", 1010)
# print(p1.name)
# print(p1.callNik())
# p1.changeNik(int(input("input nik anda: ")))
# print(p1.callNik())


class Student():
    def __init__(self, name, grade, kelas):
        self.name= name
        self.__grade = grade
        self._kelas = kelas
    def get_grade(self):
        return self.__grade
    def set_grade(self, grade):
        if(0 <= grade <= 100):
            self.__grade = grade
        else:
            print("grade must between 0 - 100")

    def get_status(self):
        if(self.__grade >= 60):
            return "good"
        else:
            return "bad"

    def __printKelas(self):
        print(self._kelas)

s1 = Student("Chandra", 80, "AA")
print(s1.get_grade())
s1.set_grade(50)
print(s1.get_grade())
print(s1.get_status())
print(s1._kelas)
# s1.__printKelas()

class Calculator():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def add(self):
        return self.number1 + self.number2
    def __multiple(self):
        return self.number1 * self.number2
    def kali(self):
        return f"hasil perkalian dari {self.number1} dan {self.number2} adalah {self.__multiple()}" 

r1 = Calculator(10, 20)
print(r1.add())
print(r1.kali())
print(r1._Calculator__multiple())
