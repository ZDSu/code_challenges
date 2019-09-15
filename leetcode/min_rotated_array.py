# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/


# runtime 28 ms, 76%; memory 12 MB, 45%
# runtime 28 ms, 57%; memory 12 MB, 60%
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0]

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]


# runtime 16 ms, 100%; memory 12.1 MB, 13%
# runtime 24 ms, 84%; memory 12.1 MB, 20%
# runtime 44 ms, 92%; memory 14.1 MB, 6%
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


# runtime 24 ms, 84%; memory 12 MB, 60%
# runtime 40 ms, 99%; memory 13.8 MB, 6%
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or nums[0] < nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1


# runtime 48 ms, 74%; memory 14 MB, 6%
# [code from solving number of rotations in rotated sorted array]
class Solution:
    def findMin(self, arr: List[int]) -> int:
        if arr[0] <= arr[-1]:
            return arr[0]

        l = 0
        r = len(arr) - 1

        while l + 1 < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid - 1]:
                return arr[mid]
            elif arr[mid] < arr[-1]:
                r = mid
            else:
                l = mid

        return arr[r]


# runtime 48 ms, 74%; memory 13.9 MB, 6%
# [someone else's code from solving number of rotations in rotated sorted array]
class Solution:
    def findMin(self, arr: List[int]) -> int:
        if not arr:
            return

        l, r = 0, len(arr)-1
        while l+1 < r:
            # mid point
            mid = (l+r)//2

            # if we have found an element that is
            # lower than the first element
            if arr[mid] < arr[0]:
                r = mid

            # all the elements from index 0 till mid index are in
            # increasing order hence we need to look in the right half
            elif arr[mid] > arr[0]:
                l = mid

        if arr[l] < arr[0]:
            return arr[l]
        elif arr[r] < arr[0]:
            return arr[r]
        else:
            return arr[0]


# test cases:
# [1,2]  returns 1
# [4,5,1,2,3]  returns 1
# [2,1]  returns 1


# more test cases
# [8, 9, 10, 2, 5, 6]  returns 3
# [2, 5, 6, 8, 9, 10]  returns 0
# [20, 2, 3, 6, 12, 13, 14, 15, 16, 17, 18, 19]  returns 1
# [3, 6, 12, 13, 14, 15, 16, 17, 18, 1, 2]  returns 9
# [10, 11, 12, 13, 14, 15, 16, 17, 1, 2, 3, 4, 5, 6]  returns 8
# [2]  returns 0
# [2, 3, 6, 12, 15, 18]  returns 0
# [2, 3]  returns 0
# [2, 3, 1]  returns 2
