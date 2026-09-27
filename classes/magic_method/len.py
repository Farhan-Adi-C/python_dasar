class Company():
    def __init__(self, employess):
        self.employess = employess

    def __len__(self): 
        return len(self.employess)

c1 = Company(["Apple", "Samsung", "Huwawei"])
print(len(c1))
