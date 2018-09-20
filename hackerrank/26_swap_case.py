# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    final = ''
    for char in s:
        if char.islower():
            final += char.upper()
        elif char.isupper():
            final += char.lower()
        else:
            final += char
    return final