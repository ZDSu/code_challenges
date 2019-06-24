# https://leetcode.com/problems/remove-element/description/
# https://leetcode.com/articles/remove-element/

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pops = []
        for i in range(len(nums)):
            if nums[i] == val:
                pops.append(i)
        for i in reversed(pops):
            nums.pop(i)
        return len(nums)


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return

        count = 0
        for num in nums:
            if num == val:
                count += 1
        for _ in range(count):
            nums.remove(val)


# from solution
# runtime 20 ms, 82%, memory 11.7, 73%
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return

        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


# runtime 20 ms, 82%; memory 11.9 MB, 7%
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i


# runtime 16 ms, 94%; memory 11.7 MB, 62%
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
