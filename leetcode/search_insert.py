# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

# test cases:
# [1], 1  returns 0
# [1,3], 1  returns 0