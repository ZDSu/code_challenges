"""
Brackets (Easy)
Determine whether a given string of parentheses (multiple types) is properly nested.

A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


def solution(S):
    parens = {'(': ')', '{': '}', '[': ']'}
    close = set(')}]')
    stack = []

    for char in S:
        if char in parens:
            stack.append(char)
        elif char in close:
            if stack:
                temp = stack.pop()
                if parens[temp] != char:
                    return 0
            else:
                return 0
    return 1


# my test cases:
# ''
# '{'
# ']'
# '}['
# '(()]('

"""
Results: https://app.codility.com/demo/results/training64VEKC-ST5/
task score 62%
correctness 33%  (pass 9/11 tests)
performance 80%  (pass 13/14 tests)

wrong: '{{{{'  returns 0
"""


def solution(S):
    parens = {'(': ')', '{': '}', '[': ']'}
    close = set(')}]')
    stack = []

    for char in S:
        if char in parens:
            stack.append(char)
        elif char in close:
            if stack:
                temp = stack.pop()
                if parens[temp] != char:
                    return 0
            else:
                return 0
    if stack:
        return 0
    return 1

"""
Results: https://app.codility.com/demo/results/trainingNHXBW2-4C7/
task score 100%
correctness 100%
performance 100%
"""
