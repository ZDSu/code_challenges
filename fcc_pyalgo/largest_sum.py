"""
Largest Sum
Take an array with positive and negative integers and find the largest continuous sum of that array.
https://leetcode.com/problems/maximum-subarray/
"""
def largest_sum(nums):
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
