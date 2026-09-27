x = {"a", "b", 1,2}

x.remove("a")
x.discard("hahaha")
y = x.pop()
print(x)

print(y)

x.clear()
# del x
print(x)