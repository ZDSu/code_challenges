# https://leetcode.com/problems/first-missing-positive/


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums or nums[-1] < 1 or nums[0] > 1:
            return 1
        if nums[0] == nums[-1]:
            return nums[0] + 1

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
        if nums[0] == nums[-1]:
            return nums[0] + 1

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
# [2,1,2,3,2]
# [2,1,2,3,1]
# [2,2,1]
# [1,2,1]
# [5,4,5]

# test cases:
# [1,1,1,1,1]
# [0,2,2,1,1]


# runtime 36 ms, 99%; memory 13.2 MB, 5%
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, 100001):
            if i not in nums:
                return i
