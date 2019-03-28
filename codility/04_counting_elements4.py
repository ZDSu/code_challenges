"""
Missing Integer (Medium)
Find the smallest positive integer that does not occur in a given sequence.

This is a demo task.

Write a function:
    def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:
- N is an integer within the range [1..100,000];
- each element of array A is an integer within the range [−1,000,000..1,000,000].

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


def solution(A):
    A = set(A)
    for i in range(1, 100001):
        if i not in A:
            return i

# Detected time complexity: O(N) or O(N * log(N))

# my test cases:
# []
# [3, -2]
# [-3, -2, -1, 0, 1]
# [-3, -2, -1, 0]
# [0]
# [2, -4, 3, 2]


"""
Results: https://app.codility.com/demo/results/trainingPAM4GS-867/
Test Score: 88%  (88/100 points)

Task Details:
- Task Score: 88%

Analysis Summary
The following issues have been detected: runtime errors.

- Correctness: 100%

- Performance: 75% (missed 1/7)
    - large_2 (shuffled sequence 1, 2, ..., 100000 (without minus))
        RUNTIME ERROR tested program terminated with exit code 1
        stderr:
        Invalid result type, int expected, <class 'NoneType'> found.
"""


def solution(A):
    A = set(A)
    for i in range(1, 100001):
        if i not in A:
            return i
    return 100001

# Detected time complexity: O(N) or O(N * log(N))

"""
Results: https://app.codility.com/demo/results/training463P6C-CS8/
task score 100%
correctness 100%
performance 100%
"""
