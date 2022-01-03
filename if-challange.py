name=input("Enter your name: ")
age=int(input("Enter your age "))
if len(name)>0:
    if age>18 and age<=35:
        print(f"Welcome to the holiday {name}")
    else:
        print(f"Sorry {name} you are not allowed  to enter to holiday party")

else:
    print("Sorry, we don't know your name. This is requirement of our ragulamin")


