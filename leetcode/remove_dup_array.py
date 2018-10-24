# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# https://leetcode.com/articles/remove-duplicates-from-sorted-array/

# Note: I kept trying to solve it by removing duplicates from array, but it just wants the length of the array if the duplicates were removed


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        j = 1
        first = nums[0]
        last = nums[-1]

        while first != last:
            if nums[j] > first:
                first = nums[j]
                j += 1
            else:
                nums.pop(j)
        return j


# some of the test cases:
# [1, 1, 2]
# [1, 2, 2]
# [1, 1, 1]
# [1, 2, 2, 2]
# []
# [0,0,1,1,1,2,2,3,3,4]


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        i = j = 0
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1

        return i + 1