# https://leetcode.com/problems/maximum-subarray/description/


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = curr = nums[0]
        
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            largest = max(largest, curr)
        return largest
