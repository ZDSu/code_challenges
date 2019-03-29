"""
BinaryGap (Easy difficulty)
Find longest sequence of zeros in binary representation of an integer.

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:
    def solution(N)
that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


def solution(N):
    N = f'{N:08b}'
    gap = 0
    temp = 0
    one = False
    for bi in N:
        if bi == '1':
            if one and temp:
                if temp > gap:
                    gap = temp
                    temp = 0
            one = not one
        else:  # bi == '0'
            if one:
                temp += 1

    return gap


# my test cases:
# 0  (binary is 00000000)  returns 0
# 2147483647  (binary is 1111111111111111111111111111111)  returns 0


"""
Results: https://app.codility.com/demo/results/trainingYS3NMC-Q57/
task score 40%
correctness 40%
performance N/A

Analysis Summary:
The following issues have been detected: wrong answers.
For example, for the input 328 the solution returned a wrong answer (got 1 expected 2).

correctness 40% (missed 9/25):
- trailing zeros: 328  returns 2
- simple3: 1162  returns 3
- medium1: 51712  returns 2
- medium2: 561892  returns 3
- medium3: 66561  returns 9
- large1: 6291457  returns 20
- large2: 74901729  returns 4
- large3: 805306373  returns 25
- large6: 1610612737  returns 28
"""


def solution(N):
    N = f'{N:08b}'
    gap = 0
    temp = 0
    one = False
    for bi in N:
        if bi == '1':
            if one and temp:
                if temp > gap:
                    gap = temp
                temp = 0
            if not one:
                one = True
        else:  # bi == 0
            if one:
                temp += 1

    return gap

# Detected time complexity: O(N) or O(N * log(N))

"""
Results: https://app.codility.com/demo/results/training463P6C-CS8/
test score 100%
task score 100%
correctness 100%
performance N/A
"""
