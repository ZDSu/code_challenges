# https://leetcode.com/problems/rotate-array/description/
# https://leetcode.com/articles/rotate-array/


# runtime 128 ms, 22%, memory 13.5 MB, 5%
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())


# doesn't pass if k > len(nums) (such as in this test case: [1,2], 3) so need to account for length--see next solution
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-k:] + nums[:-k]


# runtime 52 ms, 76%; memory 13.6 MB, 5%
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nums[:] = nums[l-k:] + nums[:l-k]
