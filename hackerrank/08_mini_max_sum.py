# https://www.hackerrank.com/challenges/mini-max-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total = sum(arr)
    max = 0
    min = arr[0] + arr[1] + arr[2] + arr[3]
    for each in arr:
        if (total - each) > max:
            max = total - each
        elif (total - each) < min:
            min = total - each
    print(min, max)

# simpler solution below.
# def miniMaxSum(arr):
#     arr.sort()
#     total = sum(arr)
#     print((total - arr[-1]), (total - arr[0]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
