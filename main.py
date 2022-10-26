from math import *

operators = ["+", "-", "*", "/", "sqrt", "^"]
variable_type = float
run_state = True


def add(operator, num1, num2):
    if operator == operators[0]:
        return variable_type(num1) + variable_type(num2)


def subtract(operator, num1, num2):
    if operator == operators[1]:
        return variable_type(num1) - variable_type(num2)


def multiply(operator, num1, num2):
    if operator == operators[2]:
        return variable_type(num1) * variable_type(num2)


def divide(operator, num1, num2):
    if operator == operators[3]:
        return variable_type(num1) / variable_type(num2)


def square_root(operator, num1):
    if operator == operators[4]:
        return sqrt(variable_type(num1))


def num_to_power(base_num, pow_num):
    result = 1.0
    for index in range(pow_num):
        result = result * base_num
    return result


def run():
    operator_input = input("Enter the operation "
                           "(ex: +, -, *, /, sqrt, ^): ")

    if operator_input == operators[0]:

        num1_input = input("Enter your first number: ")
        num2_input = input("Enter your second number: ")

        print(add(operator_input, num1_input, num2_input))

    elif operator_input == operators[1]:

        num1_input = input("Enter your first number: ")
        num2_input = input("Enter your second number: ")

        print(subtract(operator_input, num1_input, num2_input))

    elif operator_input == operators[2]:

        num1_input = input("Enter your first number: ")
        num2_input = input("Enter your second number: ")

        print(multiply(operator_input, num1_input, num2_input))

    elif operator_input == operators[3]:

        num1_input = input("Enter your first number: ")
        num2_input = input("Enter your second number: ")

        print(divide(operator_input, num1_input, num2_input))

    elif operator_input == operators[4]:

        num1_input = input("Enter your number: ")

        print(square_root(operator_input, num1_input))

    elif operator_input == operators[5]:

        base_input = int(input("Enter base number: "))
        pow_input = int(input("Enter power number: "))

        print(num_to_power(base_input, pow_input))

    else:
        print("Unknown operator.")


while run_state is True:
    run()

    response = input("Calculate again? (y or n): ")

    if response == "y":
        run_state = True
    elif response == "n":
        run_state = False
    else:
        print("Unknown Response.")
