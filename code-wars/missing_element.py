# https://www.codewars.com/kata/5a5915b8d39ec5aa18000030


def find_missing(arr1, arr2):
    arr1.sort()
    arr2.sort()
    
    for i in range(len(arr2)):
        if arr1[i] != arr2[i]:
            return arr1[i]
    return arr1[-1]