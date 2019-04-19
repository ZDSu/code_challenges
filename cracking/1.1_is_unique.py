"""
Is Unique

Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
Hints: #44, #117, #132
"""


def unique(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True


def unique(s):
    s_set = set(s)
    return not len(s) == len(s_set)


# no additional data structures
def unique(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j:
                if s[i] == s[j]:
                    return False
    return True
