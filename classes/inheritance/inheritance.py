class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(self.fname + " " +self.lname)

p1 = Person("Farhan", "Adi")
p1.printName()

class Student(Person):
    
    def __init__(self, fname, lname, nim, graduationYear):
        super().__init__(fname, lname)
        self.nim = nim
        self.graduationYear = graduationYear
    def greetingStudent(self):
        print(f"hello {self.fname}, your NIM is {self.nim}")


p2 = Student(lname="parkan", fname="chandra", nim=1010, graduationYear=2020)
p2.printName()
p2.greetingStudent()
print(p2.graduationYear)