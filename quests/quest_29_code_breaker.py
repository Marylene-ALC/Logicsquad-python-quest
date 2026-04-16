#!/usr/bin/python3

number = 42
tries = 0
max_tries = 3

while tries < 3:
    number_input = int(input("Guess the correct number: "))

    tries += 1
    remaining = max_tries - tries

    if number_input == number:
        print("You guessed the number correctly")
        break
    elif number_input > number:
        print("You went over the limit, You have", remaining, "left")
    elif number_input < number:
        print("You were under the limit, You have", remaining, "left")
#    tries += 1
else:
    print("Failed all", remaining, "tries")
