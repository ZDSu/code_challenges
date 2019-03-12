"""
Non-Repeat Elements in Array
Take a string and return character that never repeats (Note: the title says array but his directions say string)
if multiple uniques then return only the FIRST unique
Then will also solve to return EVERY element that is not repeating

https://leetcode.com/problems/first-unique-character-in-a-string/ (same challenge as for #9)
"""


def first_nonrepeat(s):
    s = s.replace(' ', '').lower()
    chars = {}

    for letter in s:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1

    for letter in s:
        if chars[letter] == 1:
            return letter

    return

print(first_nonrepeat('I Apple Ape Peels'))  # returns i
