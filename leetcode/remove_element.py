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