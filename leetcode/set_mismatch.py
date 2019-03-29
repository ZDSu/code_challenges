#


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] != i:
                res.extend([nums[i], nums[i]+1])
                return res
            i += 1

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] != i:
                res.extend([nums[i], nums[i]+1])
                return res
