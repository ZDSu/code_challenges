# https://leetcode.com/problems/permutations/


# p@thr1se solution
# runtime 48 ms, 71%; memory 13.8 MB, 5%
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, temp):
        if len(temp) == len(nums):
            self.res.append(temp[:])
            return

        for i in range(len(nums)):
            if nums[i] in temp: continue
            temp.append(nums[i])
            self.dfs(nums, temp)
            temp.pop()
