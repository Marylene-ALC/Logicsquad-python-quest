#!/usr/bin/python3

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
