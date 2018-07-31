# https://leetcode.com/problems/two-sum/description/
# solution: https://leetcode.com/articles/two-sum/


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    break
                elif nums[i] + nums[j] == target:
                    return sorted([i, j])