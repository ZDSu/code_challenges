# https://leetcode.com/problems/maximum-subarray/description/
# https://leetcode.com/articles/maximum-subarray/  (Premium)


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


# test cases [-2,1]  returns 1

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


# runtime 40 ms, 95%; memory 12.3 MB, 67%
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = temp = nums[0]

        for i in range(1, len(nums)):
            if nums[i] + temp < nums[i]:
                temp = nums[i]
            else:
                temp += nums[i]
            if temp > largest:
                largest = temp
        return largest



# Approach 1 Solution Code (see PDF)
class Solution:
    def cross_sum(self, nums, left, right, p):
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]

        p = (left + right) // 2

        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)

        return max(left_sum, right_sum, cross_sum)

    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)
