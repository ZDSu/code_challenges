# https://leetcode.com/problems/maximum-subarray/description/


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = curr = nums[0]
        
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            largest = max(largest, curr)
        return largest


# test cases [-2,1]

# beats 98.75%, takes less time to run by not using max function
# when ran again along with 2 new solutions below, runtime: 44 ms, 94%; memory: 13.6 MB, 5.5%
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        largest = nums[0]
        curr = 0

        for num in nums:
            if curr + num < num:
                curr = num
            else:
                curr += num
            if largest < curr:
                largest = curr
        return largest


# runtime: 44 ms, 94%; memory: 13.9 MB
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return

        largest = temp = nums[0]
        temp = nums[0]

        for num in nums[1:]:
            if temp + num > num:
                temp += num
            else:
                temp = num
            if temp > largest:
                largest = temp
        return largest


# runtime: 52 ms, 47%; memory: 13.7 MB
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return

        largest = temp = nums[0]

        for num in nums[1:]:
            temp = max(temp + num, num)
            largest = max(temp, largest)

        return largest
