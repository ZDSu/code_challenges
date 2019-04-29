"""
URLify

Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
EXAMPLE
Input: "Mr John Smith      ", 13
Output: "Mr%20John%20Smith"
Hints: #53, #118

https://leetcode.com/problems/move-zeroes/ (similar)
"""


def urlify(s, l):
    res = ''
    for char in s:
        if char == ' ':
            res += '%20'
        else:
            res += char
    return res


def urlify(s, l):
    arr = list(s)
    j = len(arr) - 1
    for i in range(l - 1, -1, -1):
        if arr[i] != ' ':
            arr[j] = arr[i]
            j -= 1
        else:
            arr[j - 2:j + 1] = ['%', '2', '0']
            j -= 3
    return ''.join(arr)


# if using arr instead of string since python strings are immutable
def urlify(arr, l):
    j = len(arr) - 1
    for i in range(l - 1, -1, -1):
        if arr[i] != ' ':
            arr[j] = arr[i]
            j -= 1
        else:
            arr[j - 2:j + 1] = ['%', '2', '0']
            j -= 3
    return arr
urlify(['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', ' ', ' ', ' ', ' '], 13)
