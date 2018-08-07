# 2) A magic index in an array A[0…n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index if one exists, in an array A. FOLLOW UP: What if the values are not distinct?

def magic_index(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1