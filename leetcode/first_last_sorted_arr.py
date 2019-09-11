# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/


# find first position of element in sorted array
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:  # nums[mid] >= target
                r = mid

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1


# find last position of element in sorted array
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid
            else:  # nums[mid] > target
                r = mid

        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        return -1


# pathrise assignment hackerrank solution
# runtime 72 ms, 53%; memory 13 MB, 79%
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid

        if nums[l] == target:
            left = l
        elif nums[r] == target:
            left = r
        else:
            left = -1

        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid

        if nums[r] == target:
            right = r
        elif nums[l] == target:
            right = l
        else:
            right = -1

        return [left, right]


# Pathrise solution [Find Range in a Sorted Array] (Erik/Pair Programming)
# runtime: 68ms, 79%; memory 13.1 MB, 53%
def find_bound(array, target, look_left):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            if look_left:
                if mid == 0 or array[mid-1] != target:
                    return mid
                else:
                    high = mid - 1
            else: # look_right
                if mid == len(array)-1 or array[mid+1] != target:
                    return mid
                else:
                    low = mid + 1
    return -1

class Solution(object):
    def searchRange(self, array, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start_idx = find_bound(array, target, True)
        end_idx = find_bound(array, target, False)
        return (start_idx,end_idx)


# test case: [], 0
