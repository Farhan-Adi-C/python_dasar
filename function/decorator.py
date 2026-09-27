def decorator(func): 
    def wrapper(name): 
        print("sebelum")
        print(func(name).capitalize())
        print("sesudah")
    return wrapper

@decorator
def salam(name):
    return f"halo {name}"

salam(name="Farhan")

def decorator2(func):
    def inner(*args, **kwargs):
        print("sebelum")
        print(func(*args, **kwargs))
        print("sesudah")
    return inner
@decorator2
def nyoba(name):
    return f"halo {name}"

nyoba("Adi")

def myfunction():
  return "Have a great day!"

print(myfunction.__name__)