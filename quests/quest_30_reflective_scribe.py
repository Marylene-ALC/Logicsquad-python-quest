#!/usr/bin/python3
#Quest 27 The FizzBuzz Test
#Loop through numbers 1-100 and replace multiples of 3 and 5 with specific words.
for i in range(1, 101):

    if i % 15 == 0:
        print("FizzBuzz") # replacing multiple of 15 with FuzzBuzz

    elif i % 3 == 0:     
        print ("Fizz") # replacing multiple of 3 with Fuzz

    elif i % 5 == 0:
         print("Buzz") #replacing multiple of 5 with Buzz
     

    else:
        print(f"{i}") 







#Quest28 -THE ADVENTURE GAME
#This is the starting point of the game. This function tells you the options that we have and as a user you are able to choose where to go to start playing the game.

def start():
    print("You are infront of two doors.")
    choice = input("Do you go left or right? ").lower()

    if choice == "left":
        forest()
    elif choice == "right":
        cave()
    else:
        #If the player/user input is invalid, show message and restart the game
        print("Invalid choice.")
        start()

# This function represents the forest path and gives three different options that describes how the game is played.
def forest():
    print("You enter a dark forest")
    choice = input("Do you climb a tree or keep moving around? ").lower()

    if choice == "climb":
        print("You spot a village and escape safely!")#Good ending
    elif choice == "walk":
        print("You get lost forever")#Bad ending
    else:
        print("Invalid choice.")
        forest()

 # This functions represnts the cave path. Same as the above gives you three different options constisting of both good and bad ending
def cave ():
    print("You enter a dark and scary cave")
    choice = input("Do you explore deeper or run away? ").lower()

    if choice == "explore":
        print("You find trreasure!")#Good ending
    elif choice == "run":
        print("You trip and the cave collapses ")#Bad ending
    else:
        print("Invalid choice.")
        cave()


# Start the gam by calling the start function
start()

#QUEST 30 - THE REFLECTIVE SCRIBE

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
        
# elif used to place another if condition where the input is grater than the number variable
elif number_input > number:
        print("You went over the limit, You have", remaining, "left")
    # elif used to place another if condition for when the input is less than the number variable
elif number_input < number:
        print("You were under the limit, You have", remaining, "left")
# else condition which will run if the conditions above are not met
else:
 print("Failed all", remaining, "tries")





