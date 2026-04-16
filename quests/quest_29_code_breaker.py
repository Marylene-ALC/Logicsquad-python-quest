#!/usr/bin/python3

# Declaring variables
number = 42
tries = 0
max_tries = 3

# while loop used to run the conditions and return result
while tries < 3:
    # number_input used to get input from the user
    number_input = int(input("Guess the correct number: "))

# tries += 1 used to increase the number of tries till 3 
    tries += 1
    # This is used to calculate the number of tries remaining
    remaining = max_tries - tries

# if condition used to check if the input is the same as the declared number variable
    if number_input == number:
        print("You guessed the number correctly")
        # break is used to stop the program when the condition is satisfied
        break
    # elif used to place another if condition where the input is grater than the number variable
    elif number_input > number:
        print("You went over the limit, You have", remaining, "left")
    # elif used to place another if condition for when the input is less than the number variable
    elif number_input < number:
        print("You were under the limit, You have", remaining, "left")
# else condition which will run if the conditions above are not met
else:
    print("Failed all", remaining, "tries")
