# Given an ASCII input string return a string where every whitespace delimited substring has the first character capitalized if it is alphabetic. If the first character in the string is an alphabetic character that should also be capitalized.

# For example:
# “abc 123 my dog ha$fleas” => “Abc 123 My Dog Ha$fleas”


# my solution
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the capitalizeWords function below.
def capitalizeWords(inputString):
    # iterate through string
    # when encounter space character
    # if next character is lowercase letter, make uppercase
    # return new string
    final = ''
    lower = False

    if inputString[0].isalpha():
        if inputString[0].islower():
            final += inputString[0].upper()

    for i in range(1, len(inputString)):
        if inputString[i] == ' ':
            lower = True
            final += inputString[i]
        elif lower is True:
            final += inputString[i].upper()
            lower = False
        else:
            final += inputString[i]
    return print(final)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inputString = input()

    res = capitalizeWords(inputString)

    fptr.write(res + '\n')

    fptr.close()
