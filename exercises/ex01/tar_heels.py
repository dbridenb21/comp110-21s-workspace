"""An exercise in remainders and boolean logic."""

__author__ = "730231060"


# Begin your solution here...

# Import math Library
import math

# Return the remainder of x/y

input_number: int = int(input("Enter an int:")) 
if math.remainder(input_number,7) == 0 and math.remainder(input_number,2) == 0:
    print("TARHEELS")
else: 
    if math.remainder(input_number,2) == 0: 
        print("TAR")
    else: 
        if math.remainder(input_number,7) == 0:
            print("HEELS")
        else: 
            if math.remainder(input_number, 7) != 0 and math.remainder(input_number,2) != 0:
                print("CAROLINA")


