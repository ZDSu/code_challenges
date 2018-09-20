# https://www.hackerrank.com/challenges/py-if-else/problem


#!/bin/python3

N = int(input())

if N % 2 == 1:
    print('Weird')
if N % 2 == 0:
    if 1 < N < 6:
        print('Not Weird')
    elif 5 < N < 21:
        print('Weird')
    else:
        print('Not Weird')