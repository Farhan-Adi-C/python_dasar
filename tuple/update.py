x = (1, "two", 3, True)
y = list(x)
y[1] = 2
x = tuple(y)
print(x)

z = ("hehe",)
x += z
print(x)