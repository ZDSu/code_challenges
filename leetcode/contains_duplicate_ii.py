# https://leetcode.com/problems/contains-duplicate-ii/description/
# https://leetcode.com/articles/contains-duplicate-ii  (Premium)


# beats all but one test case with Time Limit Exceeded
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if abs(i - j) <= k:
                        return True
        return False


# passes all tests
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                if i - dict[nums[i]] <= k:
                    return True
            dict[nums[i]] = i
        return False


# test cases:
# [99,99], 2
# [1,2,3,1,2,3], 2
