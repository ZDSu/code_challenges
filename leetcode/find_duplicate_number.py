# https://leetcode.com/problems/find-the-duplicate-number/
# https://leetcode.com/articles/find-the-duplicate-number/

# does not meet constant space restraint
# runtime 60 ms, 27%; memory 15.2 MB, 7%
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
