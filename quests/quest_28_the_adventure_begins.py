#!/usr/bin/python3
def start():
    print("You are infront of two doors.")
    choice = input("Do you go left or right? ").lower()

    if choice == "left":
        forest()
    elif choice == "right":
        cave()
    else:
        print("Invalid choice.")
        start()


def forest():
    print("You enter a dark forest")
    choice = input("Do you climb a tree or keep moving around? ").lower()

    if choice == "climb":
        print("You spot a village and escape safely!")
    elif choice == "walk":
        print("You get lost forever")
    else:
        print("Invalid choice.")
        forest()


def cave ():
    print("You enter a dark and scary cave")
    choice = input("Do you explore deeper or run away? ").lower()

    if choice == "explore":
        print("You find trreasure!")
    elif choice == "run":
        print("You trip and the cave collapses ")
    else:
        print("Invalid choice.")
        cave()


# Start the game
start()
