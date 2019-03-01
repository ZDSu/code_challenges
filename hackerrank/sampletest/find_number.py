"""
Question 1: Find the Number!

Given an unsorted array of n elements, find if the element k is present in the array or not.
Complete the findNumber function in the editor below. It has 2 parameters:
1. An array of integers, arr, denoting the elements in the array.
2. An integer, k, denoting the element to be searched in the array.
The function must return a string "YES" or "NO" denoting if the element is present in the array or not.
Example: findNumber([1, 2, 3, 4, 5], 1) returns 'YES'
"""

#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the findNumber function below.
def findNumber(arr, k):
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    res = findNumber(arr, k)

    fptr.write(res + '\n')

    fptr.close()
