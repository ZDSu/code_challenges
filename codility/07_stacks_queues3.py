"""
Nesting (Easy)
Determine whether a given string of parentheses (single type) is properly nested.

A string S consisting of N characters is called properly nested if:

- S is empty;
- S has the form "(U)" where U is a properly nested string;
- S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:
    def solution(S)
that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:
- N is an integer within the range [0..1,000,000];
- string S consists only of the characters "(" and/or ")".

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


def solution(S):
    # time complexity: O(N)
    stack = []
    for char in S:
        if char == ')':
            if not stack or stack[-1] != '(':
                return 0
            else:
                stack.pop()
        else:
            stack.append(char)
    if stack:
        return 0
    return 1


# my test cases:  '('  ,  ')'  ,  ''

# Results: https://app.codility.com/demo/results/trainingG8ZFZP-QVY/
# task score 100%
# correctness 100%  (pass 9/11 tests)
# performance 100%  (pass 13/14 tests)
