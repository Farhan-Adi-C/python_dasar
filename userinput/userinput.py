# name = input("Enter your name:")
# print(f"Hello {name}")
# fav1 = input("What is your favorite animal:")
# fav2 = input("What is your favorite color:")
# fav3 = input("What is your favorite number:")
# print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

condition = True
while condition == True:
    number2 = input("Your number is: ")
    try:
        number2 = float(number2)    
        condition = False
    except:
        print("wrong input, please try again")

print("thank you")
