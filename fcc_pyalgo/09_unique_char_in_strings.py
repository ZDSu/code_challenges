"""
Given a string, are all characters unique?
return True/False

Uses python built-in structures
Remember, arrays are mutable but strings are immutable

Similar: https://leetcode.com/problems/first-unique-character-in-a-string/
"""
def unique(s):
    chars = set()

    for char in s:
        if char in chars:
            return False
        chars.add(char)

    return True

print(unique('abc'))
