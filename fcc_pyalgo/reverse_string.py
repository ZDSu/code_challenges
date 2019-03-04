"""
Given a string of words, reverse all the words.
example: "This is the best"  returns "best the is This"
https://leetcode.com/problems/reverse-words-in-a-string/
"""

def reverse(s):
    return ' '.join(reversed(s.split()))


def reverse(s):
    length = len(s)
    spaces = [' ']
    words = []
    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1

    return ' '.join(reversed(words))

print(reverse('This is the best'))  # returns 'best the is This'
