# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/


# runtime 28 ms, 76%; memory 12 MB, 45%
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0]

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]


# test case: [1,2]  returns 1
