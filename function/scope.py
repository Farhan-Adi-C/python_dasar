# a variable inside a function can only use inside that function

def myFunc():
    x = 100
    def innerFunc():
        print(x)
    innerFunc()

myFunc()

# if you have a two variable with the same name inside and outside function, python will treat them as two different variable. one available in the global scope, one available in local scope. 

a = 200

def numFunct():
    a = 500
    print(a)

numFunct()

# you can make a global variable inside function
vari = "HAHAH"
def globalVar():
    global vari
    vari = "HEHE"
globalVar()
print(vari)

# nonlocal keyword make the variable at nested function will be belong to the outer function 

def cobaAja():
    coba = "HEHE"
    def Coba2():
        nonlocal coba
        coba = "WKWK"
    Coba2()
    print(coba)

cobaAja()
