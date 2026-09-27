import re
# txt = "The Beatless"
# x = re.search("^The.*Beatless$", txt)
# print(x)


# coba = "hujan di salatiga dan salatiga"
# y = re.findall("salatiga", coba)
# print(y)

# z = re.search("sala", coba)
# print(z.start())

txt = "The rain in Spain"
x = re.search("rain", txt)
print(x.group())