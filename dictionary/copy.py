favorit = {
    "fruit": "apple",
    "number": "nine",
    "color": "red"
}

favorit2 = favorit.copy()
favorit.popitem()
print(favorit2)
print(favorit)