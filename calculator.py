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
    # Evaluate - Performs proper arithmetic function based upon operator.
    if tokens[0] == "+":
        return add(tokens[1],tokens[2])

    if tokens[0] == "-":
        return subtract(tokens[1], tokens[2])

    if tokens[0] == "*":
        return multiply(tokens[1], tokens[2])  

    if tokens[0] == "/":
        return divide(tokens[1], tokens[2])

    if tokens[0] == "square":
        return square(tokens[1])

    if tokens[0] == "cube":
        return cube(tokens[1])

    if tokens[0] == "pow":
        return power(tokens[1], tokens[2])

    if tokens[0] == "mod":
        return mod(tokens[1], tokens[2])

    if tokens[0] == "q":
        return

