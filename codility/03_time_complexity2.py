"""
1. PermMissingElem (Easy)
Find the missing element in a given permutation.

An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:
    def solution(A)
that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:
- N is an integer within the range [0..100,000];
- the elements of A are all distinct;
- each element of array A is an integer within the range [1..(N + 1)].

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


def solution(A):
    A.sort()
    for i in range(1, len(A) + 1):
        if A[i - 1] != i:
            return i
    return len(A) + 1

# Detected time complexity: O(N) or O(N * log(N))

# my test cases:
# [num for num in range(1, 100000)]
# [0]
# [1, 2, 3]


# Results: https://app.codility.com/demo/results/trainingYZCNPF-BA8/
# task score: 100%
# correctness: 100%
# performance: 100%
