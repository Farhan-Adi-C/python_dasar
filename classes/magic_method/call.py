class TesClick():
    count = 0
    def __init__(self):
        pass

    def __call__(self, *args, **kwds):
        self.count += 1
        return self.count


tc1 = TesClick()
print(tc1())
print(tc1())
print(tc1())
print(tc1())

