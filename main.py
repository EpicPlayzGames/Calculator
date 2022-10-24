from math import *

operator = input("Enter the operation: ")
variable_type = float
variables = ["sqrt", "+", "-", "*", "/"]

num1 = ""
num2 = ""

if operator == variables[0]:

    num1 = input("Enter a value: ")
    print(sqrt(variable_type(num1)))

elif operator == variables[1]:

    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    print(variable_type(num1) + variable_type(num2))

elif operator == variables[2]:

    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    print(variable_type(num1) - variable_type(num2))

elif operator == variables[3]:

    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    print(variable_type(num1) * variable_type(num2))

elif operator == variables[4]:

    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    print(variable_type(num1) / variable_type(num2))

elif operator != variables:
    print("Unknown operator, please try again.")
