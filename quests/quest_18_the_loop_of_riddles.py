#!/usr/bin/python3
#Using a while loop to keep asking the user to guess secret game number repetedly  until they get it right.
secret_number = 22
guess = 0


while guess != secret_number:
    guess = int(input ("Guess Secret Number: "))
if guess > secret_number:
    print("Wrong! too high, Guess again:")
elif guess < secret_number:
    print("Wrong! too low, Guess again:")
else:
    print ("Correct")

