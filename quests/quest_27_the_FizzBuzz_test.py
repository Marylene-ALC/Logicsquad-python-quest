#!/usr/bin/python3
#Loop through numbers 1-100 and replace multiples of 3 and 5 with specific words.
for i in range(1, 101):

    if i % 15 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print ("Fizz")

    elif i % 5 == 0:
         print("Buzz")
     

    else:
        print(f"{i}")

    
    
