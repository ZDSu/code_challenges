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


# youtube solution--slower but slightly less memory used
def largest_sum(nums):
    if not nums:
        return

    largest = temp = nums[0]

    for num in nums[1:]:
        temp = max(temp + num, num)
        largest = max(temp, largest)

    return largest

print(largest_sum([7, 1, 2, -1, 3, 4, 10, -12, 3, 21, -19]))  # returns 38
