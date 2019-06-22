"""
Palindrome Permutation

Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
Hints: #106, #121, #134, #136

https://leetcode.com/problems/palindrome-permutation
https://leetfree.com/problems/palindrome-permutation.html
"""


def pal_perm(s):
    chars = {}
    for char in s:
        if char != ' ':
            if char in chars:
                if chars[char] == 1:
                    del chars[char]
                else:
                    chars[char] -= 1
            else:
                chars[char] = 1

    if len(chars) > 1:
        return False
    return True
