# https://leetcode.com/problems/first-missing-positive/


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums or nums[-1] < 1 or nums[0] > 1:
            return 1

        j = 0
        while nums[j] < 1:
            j += 1
        for i in range(1, len(nums)):
            if nums[j] != i:
                if nums[j] == nums[j - 1]:
                    j += 1
                else:
                    return i
            j += 1
        return j


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums or nums[-1] < 1 or nums[0] > 1:
            return 1

        j = 0
        while nums[j] < 1:
            j += 1
        for i in range(1, len(nums)):
            if nums[j] != i:
                if nums[j] != nums[j - 1]:
                    return i
                j += 1
            j += 1
        return j

# my test cases:
# []
# [0]
# [-1]
# [-1,-1]
# [1,2,2,3]

# test case: [1,1,1,1,1]