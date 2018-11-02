# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
# https://leetcode.com/articles/longest-continuous-increasing-subsequence/


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        subarr = [nums[0]]
        length = 1
        longest = 1
        for i in range(1, len(nums)):
            if nums[i] > subarr[-1]:
                subarr.append(nums[i])
                length += 1
            else:
                if length > longest:
                    longest = length
                subarr = [nums[i]]
                length = 1
        if length > longest:
            return length
        return longest

# test cases:
# [1, 3, 5, 7]
# [3,0,6,2,4,7,0,0]


# solution code (takes some time as my code)
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: 
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans


# another solution, much more optimal than above solutions
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        length = 1
        longest = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                length += 1
            else:
                longest = max(longest, length)
                length = 1
        return max(longest, length)