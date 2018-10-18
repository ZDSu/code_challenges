# https://leetcode.com/problems/single-number-ii/description/


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for num in nums:
            if num in seen:
                if seen[num] == 2:
                    del seen[num]
                else:
                    seen[num] += 1
            else:
                seen[num] = 1
        return seen.popitem()[0]