#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer recursively.

    Function Description:
    - The factorial of a number `n` is defined as the product of all positive integers from 1 to `n`.
    - By definition, the factorial of 0 is 1 (0! = 1).
    - The function uses recursion to calculate the factorial by reducing the problem size at each step.

    Parameters:
    - n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
    - int: The factorial of the input number `n`. Returns 1 if `n` is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the input number from the command-line arguments
f = factorial(int(sys.argv[1]))
# Print the calculated factorial
print(f)
