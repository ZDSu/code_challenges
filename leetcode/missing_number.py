# https://leetcode.com/problems/missing-number/description/
# https://leetcode.com/articles/missing-number/


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