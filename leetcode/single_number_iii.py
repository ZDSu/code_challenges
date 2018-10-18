# https://leetcode.com/problems/single-number-iii/description/


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = {}
        for num in nums:
            if num in seen:
                del seen[num]
            else:
                seen[num] = 1
        return list(seen.keys())