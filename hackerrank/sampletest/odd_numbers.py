"""
Question 2: Odd Numbers!

Given two integers, l and r, print all the odd numbers between l and r (inclusive). 
Complete the oddNumbers function in the editor below. It has 2 parameters:
1. An integer, l, denoting the left part of the range. 
2. An integer, r, denoting the right part of the range. 
The function must return an array of integers denoting the odd numbers between l and r (inclusive).
Example: oddNumbers(2, 5)  returns [3, 5]

Also see Question 3 below.
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the oddNumbers function below.
def oddNumbers(l, r):
    res = []
    if l % 2 == 0:
        for num in range(l + 1, r + 1, 2):
            res.append(num)
    else:
        for num in range(l, r + 1, 2):
            res.append(num)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    res = oddNumbers(l, r)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()


"""
Question 3:
Which of the following sorting algorithms has the best asymptotic runtime complexity? 
a. bubble sort
b. heap sort
c. selection sort
d. insertion sort
"""
