"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730231060"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

x = randint(1,4)
if x == 1: 
    fortune = "A beautiful, smart, and loving person will be coming into your life."
else:
    if x == 2:
        fortune = "Your life will be happy and peaceful." 
    else:
        if x == 3:
            fortune = "Soon life will become more interesting."
        else:
            if x == 4: 
                fortune = "There are great riches heading your way."
            
print("Your fortune cookie says... " + fortune + " Now, go spread positive vibes!")
