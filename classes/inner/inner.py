class Outer():
    def __init__(self):
        self.name = "Outer class"

    class Inner():
        def __init__(self): 
            self.name = "Inner class"

        def cetak(self):
            print("ini adalah inner")

cek = Outer()
print(cek.name)
cekInner = cek.Inner()

cekInner.cetak()


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.engine = self.Engine()

  class Engine:
    def __init__(self):
      self.status = "Off"

    def start(self):
      self.status = "Running"
      print("Engine started")

    def stop(self):
      self.status = "Off"
      print("Engine stopped")

  def drive(self):
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()