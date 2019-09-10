# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/


# find first position of element in sorted array
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:  # nums[mid] >= target
                r = mid

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1


# find last position of element in sorted array
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid
            else:  # nums[mid] > target
                r = mid

        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        return -1


# hackerrank/pathrise solution
# runtime 72 ms, 53%; memory 13 MB, 79%
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid

        if nums[l] == target:
            left = l
        elif nums[r] == target:
            left = r
        else:
            left = -1

        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid

        if nums[r] == target:
            right = r
        elif nums[l] == target:
            right = l
        else:
            right = -1

        return [left, right]


# test case: [], 0
