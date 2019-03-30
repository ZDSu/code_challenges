# https://leetcode.com/problems/set-mismatch/
# https://leetcode.com/articles/set-mismatch/


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] != i:
                res.extend([nums[i-1], nums[i-1]+1])
                return res
        return [nums[-1], nums[-1] + 1]

# my test cases:
# [1,1,3]
# [1,2,2]
# [1,2,3,5,5,4]

# test cases: 
# [2,2]  returns [2,1]
# [1,3,3]   returns [3,2]
# [3,2,3,4,6,5]   returns [3,1]
