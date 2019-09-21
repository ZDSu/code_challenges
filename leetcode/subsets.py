# https://leetcode.com/problems/subsets/


# runtime 36 ms, 92%, memory 13.8 MB, 6%
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        self.res = []
        self.dfs(nums, [], 0)
        return self.res

    def dfs(self, nums, temp, index):
        if index == len(nums):
            self.res.append(temp[:])
            return

        temp.append(nums[index])
        self.dfs(nums, temp, index + 1)
        temp.pop()
        self.dfs(nums, temp, index + 1)


# runtime 40 ms, 75%; memory 13.8 MB, 6%
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums, start_index, temp):
        self.res.append(temp[:])
        for i in range(start_index, len(nums)):
            temp.append(nums[i])
            self.dfs(nums, i + 1, temp)
            temp.pop()
