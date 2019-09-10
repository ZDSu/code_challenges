# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/


# runtime 28 ms, 76%; memory 12 MB, 45%
# runtime 28 ms, 57%; memory 12 MB, 60%
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


# runtime 16 ms, 100%; memory 12.1 MB, 13%
# runtime 24 ms, 84%; memory 12.1 MB, 20%
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


# runtime 24 ms, 84%; memory 12 MB, 60%
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or nums[0] < nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1


# test cases:
# [1,2]  returns 1
# [4,5,1,2,3]  returns 1
# [2,1]  returns 1
