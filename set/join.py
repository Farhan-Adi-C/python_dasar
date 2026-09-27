sets = {"satu", "dua", "tiga", 1, 2, 3, True}
sets2 = {"a", "b", "c", "satu"}

hehe = sets.union(sets2)
hoho = sets.intersection(sets2)
haha = sets.difference(sets2)
hihi = sets.symmetric_difference(sets2)
huhu = sets | sets2
print(hehe)
print(hoho)
print(haha)
print(hihi)
print(huhu)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)