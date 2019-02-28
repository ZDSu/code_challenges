"""
Given 2 strings, check to see if they are anagrams. An anagram is when 2 strings can be written using the exact same letters. Example: "dog" is an anagram of "god."  Note: Ignore spaces and capitalization.
https://leetcode.com/problems/valid-anagram/
"""

def anagram(s1, s2):
    """Not optimal solution since it is using a python module."""
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Return boolean for sorted match.
    return sorted(s1) == sorted(s2)


def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # check if same number of letters
    if len(s1) != len(s2):
        return False

    # count frequency of each letter
    count = {}

    # count the letters in s1 using a dictionary
    for letter in s1: 
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # do reverse for second string
    for letter in s1:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

anagram('dog', 'god')  # True
anagram('clint eastwood', 'old west action')  # True
anagram('public relations', 'crap built on lies')  # True
anagram('aa', 'bb')  # False
