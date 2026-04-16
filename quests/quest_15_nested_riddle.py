#!/usr/bin/python3

direction =  str(input("Do you want to go left or right: "))
#print("Direction is", direction)

swimDecision = str(input("Enter your decison for swimming: "))
#print("Swimming decision is", swimDecision)

if direction=="left":
    print("You have chosen to go left")
    if swimDecision=="swim":
        print("You have found the treasure")
    else:
        print("You have failed, Better luck next time")
else:
    print("Game Over, Try again")
