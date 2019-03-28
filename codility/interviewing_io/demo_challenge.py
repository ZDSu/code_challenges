"""
Missing Integer  (Medium difficulty)
Find the smallest positive integer that does not occur in a given sequence.

Write a function:
    def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:
- N is an integer within the range [1..100,000];
- each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution(A):
    if not A:
        return 1

    A.sort()

    if A[-1] < 1:
        return 1

    j = 1
    for i in range(len(A)):
        if i > 0:
            if A[i] == A[i-1]:
                continue
        if A[i] > 0:
            if A[i] != j:
                return j
        j += 1

    return j


# My test cases:
# []  returns 1
# [5, 5, 5]  returns 1

"""
Test Score: 55%  (55/100 points)
Results: https://app.codility.com/demo/results/demoG8RSUF-YUH/

Task Details:
- Task Score: 55%

Analysis Summary
The following issues have been detected: wrong answers. For example, for the input [-1000000, 1000000] the solution returned a wrong answer (got 2 expected 1).

- Correctness: 60% (missed 3/12)
    - extreme_single (a single element)
    - simple (simple test)
    - extreme_min_max_value (minimal and maximal values) [both wrong: expected 1 got 2 and expected 6 got 2]
    - positive_only (shuffled sequence of 0...100 and then 102...200) [one of two wrong: expected 101 got 2]
    - negative_only (shuffled sequence -100...-1)

- Performance: 50% (missed 4/7)
    - medium (chaotic sequences length=10005 (with minus)) [all 3 wrong: expected 111 got 997, expected 101 got 102, expected 5 got 4988]
    - large_1 (chaotic + sequence 1, 2, ..., 40000 (without minus))
    - large_2 (shuffled sequence 1, 2, ..., 100000 (without minus))
    - large_3 (chaotic + many -1, 1, 2, 3 (with minus)) [wrong: expected 10000 got 2]
"""
