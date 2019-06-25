# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


# runtime 52 ms, 66%; memory 12 MB, 70%
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(numbers) - 1
        while low < high:
            if target == numbers[low] + numbers[high]:
                return [low + 1, high + 1]
            elif target < numbers[low] + numbers[high]:
                high -= 1
            else:
                low += 1
