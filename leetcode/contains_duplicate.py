# https://leetcode.com/problems/contains-duplicate/description/
# https://leetcode.com/articles/contains-duplicate/


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