"""
Array Analysis
Given 2 arrays (assume no duplicates), is one array a rotation of another (return True/False)? Same size and elements but start index is different.

BigO = O(n)

select an indexed position in list1 and gets its value. Find same element in list2 and check index for index from there. If any variation, it is False. Getting to last item without a False means True.

https://leetcode.com/problems/rotate-string/
Along the same lines: https://leetcode.com/problems/rotate-array/
"""


def rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    key = list1[0]
    key_index = 0

    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i
            break

    if key_index == 0:
        return False

    for j in range(len(list1)):
        l2_index = (key_index + j) % len(list1)

        if list1[j] != list2[l2_index]:
            return False
    return True

print(rotation([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 1, 2, 3]))
print(rotation([4, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 4, 2, 3]))  # should return True but returns False
