# https://leetcode.com/problems/combination-sum/


# p@thr1se solution
# runtime 56 ms, 96%; memory 13.8 MB, 6%
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        self.dfs(candidates, target, [], 0)
        return self.res

    def dfs(self, candidates, remainder, temp, start):
        if remainder == 0:
            self.res.append(temp[:])
            return

        for i in range(start, len(candidates)):
            if remainder < candidates[i]: break
            temp.append(candidates[i])
            self.dfs(candidates, remainder - candidates[i], temp, i)
            temp.pop()
