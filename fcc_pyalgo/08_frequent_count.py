"""
Given an array, what is the most frequently occurring element?

Similar: https://leetcode.com/problems/top-k-frequent-elements/
"""
def most_frequent(arr):
    count = {}
    max_count = 0
    max_item = None

    for ele in arr:
        if ele not in count:
            count[ele] = 1
        else:
            count[ele] += 1

        if count[ele] > max_count:
            max_count = count[ele]
            max_item = ele

    return max_item
