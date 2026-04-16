#!/usr/bin/python3

num1 = float(input("enter the first number:"))
operator =input("enter operator (+,-,/,*)")
num2 = float(input("enter the second number:"))

if operator == '+':
     print (f"{num1}+{num2} = {num1 + num2}")

elif operator == "-":
     print (f"{num1}-{num2}  = {num1 + num2}")

elif operator == "*":
     print (f"{num1}*{num2} = {num1 + num2}")

elif operator == "/":
       if num2 != 0:
          print (f"{num1}/{num2} = {num1 / num2}")

else: 
     print ("invalid operator")
     
