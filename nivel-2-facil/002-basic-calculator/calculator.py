# Basic Calculator
# Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.

# Examples
# calculator(2, "+", 2) ➞ 4

# calculator(2, "*", 2) ➞ 4

# calculator(4, "/", 2) ➞ 2
# Notes
# If the input tries to divide by 0, return: "Can't divide by 0!"

# ---
# []: # END of instructions



def calculate( number_1: int|float, operator: str, number_2: int|float) -> int|float:
    """
    Basic calculator that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.
    Parameters:
        number_1: int|float - first number
        operator: str - mathematical operator
        number_2: int|float - second number
    """
    if operator == "+":
        return number_1 + number_2
    elif operator == "-":
        return number_1 - number_2
    elif operator == "*":
        return number_1 * number_2
    elif operator == "/":
        if number_2 != 0:
            return number_1 / number_2
        return "Can't divide by 0!"
    else:
        return "Invalid operator"


print(calculate(23.34, '*', 2))


