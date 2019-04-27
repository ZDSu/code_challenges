"""
Check Permutation

Given two strings, write a method to decide if one is a permutation of the other.
Hints: #7, #84, #722, #737

https://leetcode.com/problems/valid-anagram/description/
"""
def permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    seen = {}
    for char in s1:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1

    for char in s2:
        if char not in seen:
            return False
        seen[char] -= 1
        if seen[char] == 0:
            del seen[char]

    if not seen:
        return True
    return False


# leetcode: runtime 60 ms, 64%; memory 13.4 MB, 19%
