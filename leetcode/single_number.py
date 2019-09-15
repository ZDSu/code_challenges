# https://leetcode.com/problems/single-number/description/
# https://leetcode.com/articles/single-number/


# runtime 72 ms, 52%; memory 14.3 MB, 11%
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


# 76 ms, 33%; memory 13.8 MB, 42%
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


# 68 ms, 75%; memory 14.3 MB, 14%
def singleNumber(nums):
    count = collections.Counter(nums)
    for i in range(len(nums)):
        if count[nums[i]] == 1:
            return nums[i]


# without extra memory
# 72 ms, 52%; memory 13.5 MB, 85%
def singleNumber(nums):
    nums.sort()
    for i in range(1, len(nums), 2):
        if nums[i] != nums[i-1]:
            return nums[i-1]
    return nums[-1]


# [] is not a test case
