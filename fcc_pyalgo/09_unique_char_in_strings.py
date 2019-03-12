"""
Given a string, are all characters unique?
return True/False

Uses python built-in structures
Remember, arrays are mutable but strings are immutable

Similar: https://leetcode.com/problems/first-unique-character-in-a-string/
"""
# my solution, without clarifications
# edit solution to handle strings with spaces, which are ignored
def unique(s):
    chars = set()

    for char in s:
        if char in chars and char != ' ':
            return False
        chars.add(char)

    return True


# using python built-in structures
def unique(s):
    # clean up input string, take out spaces, make everything lowercase, take out punctuation -- depending on the problem domain and input possibilities
    s = s.replace(' ', '')

    # use a set (an unordered collection of unique elements)
    return len(set(s)) == len(s)


def unique(s):
    s = s.replace(' ', '')
    chars = set()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True

print(unique('a b cdef'))  # True
print(unique('a b cdeaf'))  # False
