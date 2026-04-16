#!/usr/bin/python3
secret_number = 42
guess = int(input("Please enter a number"))

if guess > secret_number:
    print("Number too long")
elif guess < secret_number:
    print("Number too short")
else:
    print("Correct number!")
