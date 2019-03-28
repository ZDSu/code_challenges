"""
Find the bug(s) and modify one line of code in the incorrect implementation of a function `solution` that is supposed to return the sum of all elements in the given array A which contains at most 1000 integers within range [-1000..1000].

Notice that for the example test case A = [0, 1, 2, 3, 4] the attached code is already returning the correct answer (10).
"""

def solution(A):
    ans = 0
    # for i in range(1, len(A)):
    for i in range(len(A)):
        ans = ans + A[i]
    return ans
