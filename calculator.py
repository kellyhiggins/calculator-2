"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

def calculate(string):
    """Takes string, tokenizes it to calculate it appropriately"""
    # Read - Takes string, splits it into parts.
    tokens = string.split(" ")

    tokens_num = []
    for item in tokens[1:]:
        tokens_num.append(int(item))

    # Evaluate - Performs proper arithmetic function based upon operator.
    if tokens[0] == "+":
        # return add(tokens_num[0], tokens_num[1])
        return "{:.2f}".format(reduce(add, tokens_num))

    if tokens[0] == "-":
        return "{:.2f}".format(reduce(subtract, tokens_num))

    if tokens[0] == "*":
        return "%.2f" %(reduce(multiply, tokens_num)) 

    if tokens[0] == "/":
        return "{:.2f}".format(reduce(divide, tokens_num))

    if tokens[0] == "square":
        return "{:.2f}".format(square(tokens_num[0]))

    if tokens[0] == "cube":
        return "{:.2f}".format(cube(tokens_num[0]))

    if tokens[0] == "pow":
        return "{:.2f}".format(reduce(power, tokens_num))

    if tokens[0] == "mod":
        return "{:.2f}".format(reduce(mod, tokens_num))

    if tokens[0] == "q":
        return

print calculate(raw_input("What would you like to calculate?"))
