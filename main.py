from math import *

operator = input("Enter the operation: ")
variable_type = float

num1 = ""
num2 = ""

if operator == "sqrt":

    num1 = input("Enter a value: ")
    print(sqrt(variable_type(num1)))

elif operator == "-":

    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    print(variable_type(num1) - variable_type(num2))

elif operator == "*":

    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    print(variable_type(num1) * variable_type(num2))

elif operator == "/":

    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    print(variable_type(num1) / variable_type(num2))

elif operator == "+":

    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    print(variable_type(num1) + variable_type(num2))

elif operator != "sqrt" or "+" or "-" or "*" or "/":
    print("Unknown operator, please try again.")
