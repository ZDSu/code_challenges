# https://leetcode.com/problems/move-zeroes/description/
# https://leetcode.com/articles/move-zeroes/


# doesn't pass second test case below
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums

        i = j = 0
        for num in nums:
            if j < len(nums):
                if num == 0:
                    while nums[j] == 0:
                        j += 1
                    nums[i] = nums[j]
                nums[j] = 0
                i += 1
                j += 1
            else:
                num = 0


# test cases:
# [0]
# [0, 0]


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        while i < j:
            nums[i] = 0
            i += 1


# Another solution from Andrii
# Function which pushes all
# zeros to end of an array.
def pushZerosToEnd(arr):
    count = 0 # Count of non-zero elements
    n = len(arr)
    # Traverse the array. If element 
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    for i in range(n):
        if arr[i] != 0:             
            # here count is incremented
            arr[count] = arr[i]
            count+=1
     
    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all 
    # elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1
    return arr

print(pushZerosToEnd([0,0]))


# best solution according to leetcode (adapted from their C++ solution)
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


# another solution, similar to the best leetcode solution
# (submitted twice in a row, returned 48 msec then 80 msec.. wth!)
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        i = j = 0
        
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                i += 1