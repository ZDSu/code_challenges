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
        # did again and now popitem() is the faster solution


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return seen.pop()