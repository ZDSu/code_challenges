"""
Common Elements in Two Sorted Arrays
Return the common elements (as an array) between two sorted arrays of integers (ascending order).
Example: [1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10] returns [1, 4, 9]
Similar but not sorted: https://leetcode.com/problems/intersection-of-two-arrays/
"""


def common_elements(arr1, arr2):
    res = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1  # his code was j += 2 but that's wrong
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            i += 1

    return res

print(common_elements([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10]))
