# https://www.codewars.com/kata/577a98a6ae28071780000989/


def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


# another solution
def min(arr):
    return sorted(arr)[0]

def max(arr):
    return sorted(arr)[-1]


# not using built-in methods
def min(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low

def max(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high