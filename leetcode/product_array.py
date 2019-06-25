# https://leetcode.com/problems/product-of-array-except-self/


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            temp = None
            for j in range(len(nums)):
                if i != j:
                    if temp is not None:
                        temp *= nums[j]
                    else:
                        temp = nums[j]
            output.append(temp)
        return output


# test cases:
# [9,0,-2]   returns [0,-18,0]
# [-1,-1,1,-1,-1,1,-1,-1,-1,1,1 ... forever]  get Time Limit Exceeded
