# https://leetcode.com/problems/single-number/description/
# https://leetcode.com/articles/single-number/


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for num in nums:
            if num in seen:
                del seen[num]
            else:
                seen[num] = 1
        return list(seen.keys())[0]
        # return seen.popitem()[0]   # from solution, but runtime is a lot worse for some weird reason