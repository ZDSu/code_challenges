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


# test cases [-2,1]

# beats 98.75%, takes less time to run by not using max function
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        largest = nums[0]
        curr = 0

        for num in nums:
            if curr + num < num:
                curr = num
            else:
                curr += num
            if largest < curr:
                largest = curr
        return largest