# https://www.hackerrank.com/challenges/balanced-brackets/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    if len(s) % 2 == 0:
        for i in range(len(s) // 2):
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        if s == '':
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()


# another solution
def isBalanced(s):
    if len(s) % 2 != 0:
        return 'NO'
    
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ']':
            if len(stack) == 0:
                return 'NO'
            elif stack[-1] == '[':
                stack.pop()
            else:
                return 'NO'
        elif s[i] == '}':
            if len(stack) == 0:
                return 'NO'
            elif stack[-1] == '{':
                stack.pop()
            else:
                return 'NO'
        else:
            if len(stack) == 0:
                return 'NO'
            elif stack[-1] == '(':
                stack.pop()
            else:
                return 'NO'
    if len(stack) > 0:
        return 'NO'
    return 'YES'