favorit = {
    "fruit": "apple",
    "number": "nine",
    "color": "red"
}


[print(x) for x in favorit]

[print(favorit[x]) for x in favorit]
[print(x) for x in favorit.values()]
[print(x, y) for x, y in favorit.items()]