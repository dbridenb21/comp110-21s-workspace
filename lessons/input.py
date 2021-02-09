"""A program to demonstrate user input and variables."""

print("Wow, " + input("Who are you? ") + ", you rock!")
print(input("Who are you? ") + " have a great day!")

# Import math Library
import math

# Return the remainder of x/y

input_number: int = int(input("Enter an int:")) 
if math.remainder(input_number,2) == 0: 
    print("TAR")
else: 
    if math.remainder(input_number,7) == 0:
    print("HEELS")
    else: 
        if math.remainder(input_number,7) and math.remainder(input_number,2):
        print("TARHEELS")
        else: 
            if math.remainder(input_number, 7) and math.remainder(input_number,2) != 0:
            print("CAROLINA")