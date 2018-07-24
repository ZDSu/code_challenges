"""
https://www.codewars.com/kata/mylanguages/train/python

Given a list of languages and your respective test results, return the list of languages where your test score is at least 60, in descending order of the results.

Note: There will be no duplicate values.

Examples
{"Java": 10, "Ruby": 80, "Python": 65}  --> ["Ruby", "Python"]
{"Hindi": 60, "Dutch" : 93, "Greek": 71} --> ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20}   --> []
"""


def my_languages(results):
    final = {}
    for k,v in results.items():
        if results[k] >= 60:
            final[k] = v
    return sorted(final, key=final.get, reverse=True)