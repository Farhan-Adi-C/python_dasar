import sys


print(sys.version)

x = 20
y = 5
X = 10

if x > y:
    print("haha")
else:
    print("hehe")
    



def coba():
    x = """
bbbbb
aaaaa
ccccc
"""
    print(x)
coba()

# for q in "banana":
#   print(q)

a = " haheho \"coba\" wkwk"
b = [1]

print(a[1:3])
print(a.upper())
print(a.strip()) 
print(a.endswith("wk")) 
print(bool(b))
"""
     *
    ***
   *****
  *******
 *********
***********
  """

c = "ternary" if x < 10 else "ternary2"
print(c)

import cowsay

cowsay.cow("Good Mooooorning!")