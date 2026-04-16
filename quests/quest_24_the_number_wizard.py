#!/usr/bin/python3

def ask_for_age():
   your_age = int(input("What is your age:"))
   return your_age
def can_they_vote(your_age):
    if your_age>= 18:
        print("You can vote!")
    else:
        print("you can not vote")

user_age = ask_for_age()
can_they_vote(user_age)


