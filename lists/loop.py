lists = ["one", 2, "three", "four", 5, "six"]

for x in lists:
    print(x)

# for i in range(len(lists)):
#     print(lists[i])
# i = 0
# while i < len(lists): 
#     print(lists[i])
#     i += 1

[print(x) for x in lists]