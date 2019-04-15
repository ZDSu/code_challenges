"""
https://www.codewars.com/kata/517abf86da9663f1d2000003/

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

Examples:
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
"""


def to_camel_case(text):
    if not text:
        return ''

    res = ''
    upper = False
    for char in text:
        if char == '-' or char == '_':
            upper = True
        else:
            if upper:
                res += char.upper()
                upper = False
            else:
                res += char
    return res
