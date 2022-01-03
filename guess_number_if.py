answer=5
guess=int(input("Please guess the number between 1 and 10 "))
if guess !=answer:
    if guess<answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
        guess=int(input())
        if guess==answer:
            print("Well done")
        else:
            print("Sorry, you didn't have a right guess")
else:
    print("You got it at first time. ")



# if guess<answer:
#     print("Please guess higher")
#     guess=int(input())
#     if guess==answer:
#         print("Well done , you guessed it")
#     else:
#         print("Sorry, you guessed incorectly")
# elif guess>answer:
#     print("Please guess lower ")
#     guess = int(input())
#     if guess == answer:
#         print("Well done , you guessed it")
#     else:
#         print("Sorry, you guessed incorectly")
# else:
#     print("You got this at first time ")
