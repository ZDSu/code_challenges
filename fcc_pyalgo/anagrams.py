"""
Given 2 strings, check to see if they are anagrams. An anagram is when 2 strings can be written using the exact same letters. Example: "dog" is an anagram of "god."  Note: Ignore spaces and capitalization.
"""

def anagram(s1, s2):
    """Not optimal solution since it is using a python module."""
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Return boolean for sorted match.
    return sorted(s1) == sorted(s2)

anagram('dog', 'god')  # True
anagram('clint eastwood', 'old west action')  # True
anagram('public relations', 'crap built on lies')  # True
anagram('aa', 'bb')  # False
