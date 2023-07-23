"""Kellye Richards
Final Project - Calculator
CIT 432
--------------------------
For the final project, you are to write a calculator program in Python with the following characteristics:
It must be at least 50 lines of code excluding comments
It must have the following functions:+,-,*,/, SQRT, and work with decimal numbers.
It must be all text, no high resolution graphics
It must automatically copy the result to the operating system clipboard
It must work as a functional calculator (calculations can be entered over and over)
Please submit the source code only (.py) from IDLE , no object code (I will compile on receipt)
"""

# Allows math functions
import math
# Allows system commands
import subprocess
# Allows functions for Windows (in this program)
import sys

# It must have the following functions:+,-,*,/, SQRT, and work with decimal numbers.
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        # division by zero error
        return "Division by zero not possible!"

def square_root(num1):
    if num1 >= 0:
        return math.sqrt(num1)
    else:
        return "Invalid input"

# Dictionary for operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "√": square_root,
}

#It must automatically copy the result to the operating system clipboard (windows for this program)
def clipboard_copy(text):
    if sys.platform.startswith("win"):
        # sub function executes echo and clip commands
        subprocess.run("echo " + text.strip() + "| clip", shell=True)

# Calculator function
def calculator():
    while True:
        number1 = float(input("Enter the first number (or 'q' to quit): "))
        # This section breaks the loop if q is the input
        if number1 == 'q':
            break
        # iterate through the operations dictionary and show on screen
        for sign in operations:
            print(sign)
        
        to_continue = True

        while to_continue:
            operation_sign = input("Choose an operation from the line above to be performed: ")

            # This section breaks the loop if q is the input
            if operation_sign == 'q':
                to_continue = False
                break

            number2 = float(input("Enter another number: "))

            #Get value/key
            calc_function = operations.get(operation_sign)

            if calc_function:
                solution = calc_function(number1, number2)
                print(f"{number1} {operation_sign} {number2} = {solution}")

                # Copy the result to the clipboard
                clipboard_copy(str(solution))

                number1 = solution
            else:
                print("Invalid!")
    # Exit message
    print("Exiting calculator...")

calculator()