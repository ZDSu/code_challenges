# Given an input string add some factor to each alphabetic character and return the string. Non-alphabetic characters should remain unchanged in the return string. Characters wrap around to the beginning of the alphabet. Uppercase and lowercase characters are 2 independent sets independently, uppercase chars always wrap around to upper case, lowercase wrap around to lowercase.

# You can hardcode the values into the main function.

# Example:
# rotateValue: 1 
# input string:    "bcd xyz $%^"
# output string: "cde yza $%^" 

# rotateValue: 3 
# input string:   "BCD xyz !@#" 
# output string: "EFG abc !@#" 


# my solution
# Note: This one was still in Python and not Python3 for some reason...

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the rotateCharacters function below.
def rotateCharacters(shiftValue, inputString):
    # initiate final output string
    # iterate through the string
    # if letter, convert to ascii value
    # add rotateValue ascii value
    # if ascii value outside of alpha range, need to start at beginning
    # append new character to final output string
    # ascii values: A-Z = 65-90, a-z = 97-122
    if shiftValue == 0:
        return inputString

    final = ''

    for i in range(len(inputString)):
        if inputString[i].isalpha():
            temp = ord(inputString[i]) + shiftValue
            if temp > 122 and (123 > ord(inputString[i]) > 96):
                temp = 97 + (temp - 123)
            elif temp > 90 and (91 > ord(inputString[i]) > 66):
                temp = 65 + (temp - 91)
            final += chr(temp)
        else:
            final += inputString[i]
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    shiftValue = int(raw_input().strip())

    inputString = raw_input()

    res = rotateCharacters(shiftValue, inputString)

    fptr.write(res + '\n')

    fptr.close()
