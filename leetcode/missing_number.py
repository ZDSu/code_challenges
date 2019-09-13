# https://leetcode.com/problems/missing-number/description/
# https://leetcode.com/articles/missing-number/


# runtime 128 ms, 22%; memory 12.8 MB, 37%
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        for each in sorted(nums):
            if each != current:
                return each - 1
            current += 1
        return each + 1


# runtime 116 ms, 60%; memory 13.2 MB, 7%
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = set(nums)
        for i in range(len(nums) + 1):
            if i not in numbers:
                return i


# test cases:
# [0]  returns 1
# [1]  returns 0
# [0,1]  returns 2
