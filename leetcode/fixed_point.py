"""
Fixed Point
Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i. Return -1 if no such i exists.

Example 1:
Input: [-10,-5,0,3,7]
Output: 3
Explanation: For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.

Example 2:
Input: [0,2,5,8,17]
Output: 0
Explanation: A[0] = 0, thus the output is 0.

Example 3:
Input: [-10,-5,3,4,7,9]
Output: -1
Explanation: There is no such i that A[i] = i, thus the output is -1.

Note:
1. 1 <= A.length < 10^4
2. -10^9 <= A[i] <= 10^9

My custom test case: [-10, 1, 2, 5, 10]
"""

# runtime 72 ms, 87%; memory 14.9 MB, 25%
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i in range(len(A)):
            if A[i] == i:
                return i
        return -1


# runtime 64 ms, 99%; memory 15 MB, 25%
# runtime 68 ms, 95%; memory 15.2 MB, 25%
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        left = 0
        res = right = len(A) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] == mid:
                if mid < res:
                    res = mid
                    right = mid
            elif A[mid] > mid:
                right = mid
            else:
                left = mid

        if A[left] == left:
            return left
        if A[right] == right:
            return right
        return -1


# runtime 76 ms, 62%; memory 15.2 MB, 25%
# doesn't make sense why this is slower than above
# runtime 84 ms, 9%; memory 15.3 MB, 25%
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        left = 0
        res = right = len(A) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] == mid:
                res = mid
                right = mid
            elif A[mid] > mid:
                right = mid
            else:
                left = mid

        if A[left] == left:
            return left
        if A[right] == right:
            return right
        return -1

# [] is not a test case thankfully!
