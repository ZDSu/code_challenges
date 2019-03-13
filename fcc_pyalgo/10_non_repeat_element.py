"""
Non-Repeat Elements in Array
Take a string and return character that never repeats (Note: the title says array but his directions say string)
if multiple uniques then return only the FIRST unique
Then will also solve to return EVERY element that is not repeating

https://leetcode.com/problems/first-unique-character-in-a-string/
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


def nonrepeats(s):
    s = s.replace(' ', '').lower()
    chars = {}
    uniques = []

    for letter in s:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1

    y = sorted(chars.items(), key=lambda x: x[1])

    for item in y:
        # if item[1] == y[0][1]:
        if item[1] == 1:
            uniques.append(item[0])

    return uniques

# Note, his code is wrong (line 44). this will return all elements that occur the same amount of times as the least occuring element. For example, nonrepeats('Is Applie Ape Peels') will return ['i', 's', 'a', 'l']

print(nonrepeats('I Apple Ape Peels'))  # returns [('i', 1), ('s', 1)]
