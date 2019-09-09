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


# runtime 32 ms, 86%; memory 12.1 MB, 100%
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if nums[l] < target:
            return l + 1
        else:
            return l


# test cases:
# [1], 1  returns 0
# [1,3], 1  returns 0
# [1,3], 0  returns 0
