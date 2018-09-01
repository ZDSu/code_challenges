# https://leetcode.com/problems/jump-game/description/
# solution: https://leetcode.com/articles/jump-game/


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0
        for i, n in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + n)
        return True
        