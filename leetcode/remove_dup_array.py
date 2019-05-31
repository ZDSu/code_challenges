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


# test cases:
# [1,1]
# [1, 1, 2]
# [1, 2, 2]
# [1, 1, 1]
# [1, 2, 2, 2]
# []
# [0,0,1,1,1,2,2,3,3,4]
# [1]


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


# runtime 56 ms, 95%; memory 14.7 MB, 5%
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

        single = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[single]:
                single += 1
                nums[single] = nums[i]
        return single + 1


# runtime 60 ms, 80%; memory 14.7 MB, 5%
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[j + 1], nums[i] = nums[i], nums[j + 1]
                j += 1
        return j + 1


# runtime 60 ms, 84%; memory 14.9 MB, 33%
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        i = j = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1
