class Vechile():
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
      print("Move")

class Car(Vechile):
    pass
    def move(self):
      print("Car!")
  
class Boat(Vechile):
 pass
 def move(self):
   print("Boat")

class Plane(Vechile):
  pass



car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()