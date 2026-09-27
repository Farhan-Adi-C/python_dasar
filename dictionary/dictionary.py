favorit = {
    "fruit": "apple",
    "number": "nine",
    "color": "red"
}

favorit["color"] = "blue"
[print(x) for x in favorit]
print(favorit)
print(favorit["color"])
print(favorit.get("fruit"))
print(favorit.keys())
print(favorit.values())
print(favorit.items())