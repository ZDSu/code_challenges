# https://leetcode.com/problems/contains-duplicate/description/
# https://leetcode.com/articles/contains-duplicate/


# runtime 48 ms, 66%; memory 18.5 MB, 26% (same results as the one-liner)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numbers = set()
        for each in nums:
            if each in numbers:
                return True
            numbers.add(each)
        return False


# one line
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         return len(set(nums)) < len(nums)


# another one-liner
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(nums) == len(set(nums))


# runtime 48 ms, 66%; memory 18.6 MB, 26%
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
