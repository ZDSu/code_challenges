# https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for each in arr:
        if each == 0:
            zero += 1
        elif each > 0:
            pos += 1
        else:
            neg += 1
    print(pos / len(arr))
    print(neg / len(arr))
    print(zero / len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)