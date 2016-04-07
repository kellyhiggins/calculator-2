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
        tokens_num.append(float(item))

    # Evaluate - Performs proper arithmetic function based upon operator.
    if tokens[0] == "+":
        return add(tokens_num[0], tokens_num[1])

    if tokens[0] == "-":
        return subtract(tokens_num[0], tokens_num[1])

    if tokens[0] == "*":
        return multiply(tokens_num[0], tokens_num[1]) 

    if tokens[0] == "/":
        return divide(tokens_num[0], tokens_num[1])

    if tokens[0] == "square":
        return square(tokens_num[0])

    if tokens[0] == "cube":
        return cube(tokens_num[0])

    if tokens[0] == "pow":
        return power(tokens_num[0], tokens_num[1])

    if tokens[0] == "mod":
        return mod(tokens_num[0], tokens_num[1])

    if tokens[0] == "q":
        return

print calculate(raw_input("What would you like to calculate?"))