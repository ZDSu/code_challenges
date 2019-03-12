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

print(most_frequent([1,3,3,3,2,1,1,1]))  # returns 1
print(most_frequent([1,3,3,3,3,2,1,1,1]))  # returns 3 but should return 1 and 3; he doesn't take care of this edge case
